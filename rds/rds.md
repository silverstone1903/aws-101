### RDS
#### DBeaver

DB'ye erişmek için [DBeaver](https://dbeaver.io/download/) kurulması gereklidir. **Database** -> **New Database** seçilir ve ilgili ayarlar doldurulur.


<img src="https://dbeaver.com/wp-content/uploads/2022/03/Screen-Shot-2022-03-03-at-11.52.55-AM.png">

<br>

**Host**: AWS'deki DB host
**Database**: postgres
**Username**: postgres
**Password**: DB için belirlediğiniz şifre

Doldurduktan sonra **Finish** ile bağlantı kurulumu tamamlanır.

### Python ile *insert*
Python ([db.py](db.py)) kullanmak isterseniz aşağıdaki paketlerin yüklü olması gerekmektedir.

```
pandas
psycopg2
sqlalchemy
```

Paketleri yüklemek için;
```bash
pip install pandas psycopg2 sqlalchemy 
```

DB oluşturulduktan sonra [db.py](db.py) dosyasındaki `host` ve `password` değişkenleri doldurultuktan sonra komut istemci ile (command prompt) aws-101 klasörüne gidilir ve `python rds\db.py` çalıştırılır.

