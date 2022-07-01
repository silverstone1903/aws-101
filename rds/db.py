import pandas as pd
import psycopg2
from sqlalchemy import column, create_engine
import io
import warnings
import time

warnings.filterwarnings("ignore")


def psql_insert(engine, table_name, df):
    conn = engine.raw_connection()
    cur = conn.cursor()
    output = io.StringIO()
    df.to_csv(output, sep="\t", header=False, index=False)
    output.seek(0)
    contents = output.getvalue()
    cur.copy_from(output, table_name, null="")
    conn.commit()


host = ""
db = "postgres"
user = "postgres"
password = ""
engine = create_engine(
    "postgresql+psycopg2://{user}:{password}@{host}:5432/{db}".format(
        user=user, password=password, host=host, db=db
    )
)
print("Connected to PostgreSQL")
df = pd.read_parquet("rds/df.parquet")


# create ddl codes using pandas
table = "transactions"
column = "Description"
ddl = pd.io.sql.get_schema(df, table, con=engine)
print(ddl)


# create table using dtypes
engine.execute("DROP TABLE IF EXISTS {0}".format(table))
print("Dropped table if exists")
engine.execute(ddl.replace("CREATE TABLE", "CREATE TABLE IF NOT EXISTS"))
print("Created table")
start = time.process_time()
psql_insert(engine, table, df)
print(time.process_time() - start)
print("Data insert completed.")

q = """
    alter table {0} add column ts tsvector
    generated always as (to_tsvector('simple', '{1}')) stored
    """.format(
    table, column
)
engine.execute(q)
print("TSVector created for {}.".format(column))

q = """
create index ts_idx on
{0}
using GIN (ts)
""".format(
    table
)
engine.execute(q)
print("Index created for ts.")

q = """
CREATE EXTENSION IF NOT EXISTS pg_trgm;
"""
engine.execute(q)
print("Extension created for pg_trgm.")
print("Done.")
