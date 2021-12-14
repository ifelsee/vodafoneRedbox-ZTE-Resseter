 # vodafoneRedbox-ZTE-Resseter
Version __0.1.0__
### Bilgilendirme
Vakit bulduğumda servis dosyasını kuruluma ekleyeceğim ancak şuan için bilgisyar her başlattığınızda progarmı da el ile başlatmanız gerek.

### Açıklama 
Vodafone Redbox, ZTE modemlerdeki bağlantı kesilmelerini izler. 
Bağlantı kesilmesi 4 saniyeyi geçerse modem arayüzüne bağlanır ve bağlantıyı yeniler.
Müdehale ettiği tüm kesintileri log dosaysı içine tarih ve saatini ile beraber kayıt eder.
Not  Bağlantının yenilenmesi ip adresinizi değiştirir. 
### kullanım
#### Dosyayı indiriyoruz 
 ``` $ git clone https://github.com/ifelsee/vodafoneRedbox-ZTE-Resseter```
 
 ``` $ cd vodafoneRedbox-ZTE-Resseter/```
 #### run.sh'u çalışabilir hale getiriyoruz 
 ``` $ chmod +x run.sh```
 
 #### Gereksinimlerin yüklenimi  
Eğer sisteminizde geckodrive yoksa gerekli paketlerin yüklenmesi için terminalde işlem yapmanız gerek. 
 ``` $ ./run.sh```
 
![image](https://user-images.githubusercontent.com/49848935/145933227-fa8fda27-a1e8-491c-af1b-da92ac6e9e3f.png)
Enter'e bası ve paketlerin yüklenmesi için yetki 
Dilerseniz geckodrive'ı /usr/local/bin adresinde bulabilirsiniz.

#### Manuel yükleme için aşağıdaki kodları kullanın 
------



        sudo apt-get -y install python3-pip
        pip3 install selenium
        wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux32.tar.gz
        sudo sh -c 'tar -x geckodriver -zf ./geckodriver-v0.30.0-linux32.tar.gz -O > /usr/local/bin/geckodriver'
        sudo chmod +x /usr/local/bin/geckodriver
        rm geckodriver-v0.30.0-linux32.tar.gz*

## çalıştırma 
### Normal çalıştırma: 
```$ ./run.sh <modem arayüz şifreniz>```
### Arka planda çalıştırma.
kodun sonuna & ekliyoruz
```$ ./run.sh <modem arayüz şifreniz> &```


 
 ![image](https://user-images.githubusercontent.com/49848935/145935330-2012808c-3c0d-4cda-a23e-040cc7f96307.png)
 
 Şuanda prgramımız arka planda çalışıyor. 
 ### Arkaplanda çalışan progamı sonlandırma 
 terminalde verilen pid kullanarak aşşağıdaki komutu çalıştırıyoruz.
 ```$ kill <pid> ```
 
 ![image](https://user-images.githubusercontent.com/49848935/145935693-a0bbf889-5f92-4c02-ad59-920e74aa83c1.png)

Aynı komutu tekrar girersek komutun kapatılmış olduğunu görebiliriz 

![image](https://user-images.githubusercontent.com/49848935/145935822-8e724bd1-3957-49a6-b636-004d79c4a0c3.png)


 
