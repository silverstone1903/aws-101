### Linux/Mac Kullanıcıları 
1. Terminal uygulaması açılır.
2. `ssh -i /path/to/your/keypair.pem user@server-ip` komutu yazılır.
2.1 Örneğin: `ssh -i /home/youruser/keypair.pem ec2-user@123.123.123.123`
3. Unprotected private key file hatası almanız durumunda `chmod 400  /home/youruser/keypair.pem` komutu yazılır.

Ayrıca instance'a sağ tıklayıp (ya da actions menüsünden) connect derseniz ssh sekmesi altında hazır kodu bulabilirsiniz.
![](https://asf.alaska.edu/wp-content/uploads/2019/03/cloud-recipe-image-1-2000x1125.jpg)

### Windows Kullanıcıları
Windows kullanıyorsanız eğer putty.exe ve puttygen.exe indirmeniz gerekmektedir. Putty kullanarak nasıl ssh yapacağınız [AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html) sayfasında anlatılmıştır.

Putty indirmek için;
* [MSI installer (Putty ve puttygen bir arada)](https://www.puttygen.com/download-putty)
* [putty.exe](https://puttygen.com/download.php?val=13)
* [puttygen.exe](https://puttygen.com/download.php?val=49)

Bir diğer alternatif ise Windows 10 altında kullanılabilen WSL2. 

EC2 key-pair oluştururken gerekli ayarlar;

![](https://assets.cloudacademy.com/bakery/media/uploads/content_engine/image-20220531141451-7-68b98e35-3764-4380-a055-7e5e11b4d903.png)

<br>
<br>

Puttygen açılır ve **Load** butonuna basılır. Açılan ekrandan **All Files** seçilir. 
![](https://assets.cloudacademy.com/bakery/media/uploads/lab-step/blobid2-33284b50-e60d-4adc-9ca0-80400a29ba75.png)

<br>

All files seçildikten sonra AWS'ten indirilen *.pem* uzantılı dosya seçilir. 
![](https://assets.cloudacademy.com/bakery/media/uploads/lab-step/blobid4-183da0e6-7348-4594-8dd0-69ea3f7056df.png)

**OK** butonuna tıklanır ve **Save private key** denilerek oluşturulan private key kaydedilir.

Sonraki adımda putty.exe açılır ve host name kısmına instance'a ait bağlantı adresi girilir. (Connection type **SSH** olmalıdır).

![](putty-connect-step1-4ba34dd1-377c-4f0c-9bd2-c6e63c909cc4.jpg)

<br>

Sol menüde bulunan **SSH** sekmesine gidilir ve **browse** denilerek kaydedilen **private key** seçilir.
![](blobid0-9519ff3f-2934-46d2-8ca0-d81cc43c6106.png)

<br>

![](https://assets.cloudacademy.com/bakery/media/uploads/blobid0-2e0e20fd-e8ff-433b-acc7-a323f92bb06e.png)


Sunucuya bağlandıktan sonra metadata'yı çekmek için;

```
curl http://169.254.169.254/latest/meta-data/
curl http://169.254.169.254/latest/meta-data/instance-id
curl http://169.254.169.254/latest/meta-data/instance-type
curl http://169.254.169.254/latest/meta-data/public-ipv4
```


User Data için;
```
curl http://169.254.169.254/latest/user-data
```