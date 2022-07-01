### Docker ile RStudio Kurulumu
Amazon AMI kullanılarak EC2 ile bir sanal makine oluşturulur. Security Group altından 22 ve 8787 portlarına izin verilir. 


Sunucuya SSH ile bağlandıktan sonra, RStudio kullanmak için Docker kurulumu yapılır.
```bash
# Docker kurulumu
sudo su
yum update
yum install docker -y
```
<br>

Docker kurulumu tamamlandıktan sonra servis başlatılır. 

```bash
# docker servisinin başlatılması ve kontrol edilmesi
systemctl enable docker.service
systemctl start docker.service
systemctl status docker.service
```

Servis durumunun active (running) olması beklenir. `systemctl status docker.service` çıktısı aşağıdaki gibi olmalıdır.


```bash
[root@ip-0-0-0-0 ec2-user]: systemctl status docker.service
● docker.service - Docker Application Container Engine
   Loaded: loaded (/usr/lib/systemd/system/docker.service; enabled; vendor preset: disabled)
   Active: active (running) since Tue 2022-06-28 10:55:22 UTC; 5s ago
     Docs: https://docs.docker.com
  Process: 2833 ExecStartPre=/usr/libexec/docker/docker-setup-runtimes.sh (code=exited, status=0/SUCCESS)
  Process: 2832 ExecStartPre=/bin/mkdir -p /run/docker (code=exited, status=0/SUCCESS)
 Main PID: 2836 (dockerd)
    Tasks: 8
   Memory: 27.8M
   CGroup: /system.slice/docker.service
           └─2836 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock --default-ulimit nofile=32768:65536
```

Rstudio kurulumu için aşağıdaki komutları çalıştırılır.

```bash
docker run --name rstudio -d -e PASSWORD=sifreniz --rm -p 8787:8787 rocker/tidyverse
```

Docker sorunsuz bir şekilde çalıştıktan sonra sunucuya ait IP adresi ile RStudio'ya erişilir.

`public_IPV4:8787`

<br>

```bash
# Docker volume kullanılarak RStudio'nun lokal dosyalara ulaşması sağlanır.
docker run --name rstudio -d -e PASSWORD=sifreniz -p 8787:8787 -v /home/ec2-user/:/home/rstudio/rstudio_docker rocker/tidyverse 
```
<br>

Son olarak çalışma bittikten sonra docker container durdurulur. 

```bash
docker stop rstudio
```