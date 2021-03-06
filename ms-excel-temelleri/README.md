# Microsoft Excel Temelleri
Bu repo [BTK Akademide](https://www.btkakademi.gov.tr/portal/) bulunan Sayın [Kubilay Taştutar](https://www.linkedin.com/in/kubilay-tastutar-53a83898/)'ın anlatımı ile hazırlanan [Microsoft Excel Temelleri](https://www.btkakademi.gov.tr/portal/course/microsoft-excel-temelleri-13897#!/about) kursu takip edilirken alınan notları içermektedir.

## Giriş

Karmaşık hesaplama ve analizler yapılabilir görsel veri setleri oluşturulabilir.

Excel kitabındaki sayfaların içerisinde bulunan hücrelere veriler eklenir.

## Sayfa işlemleri
Silinen sayfa geri gelmez!

Sayfa ismi üzerinde sağ tık ile taşıma işlemleri gerçekleştirilebilir. Farklı bir excel kitabına taşıma veya kopyalama yapılabilir.

## Hücre, Satır, Sütun işlemleri

Seçme, kesme, kopyalama işlemleri hem hücre hem satır hem de sütun için gerçekleştirilebilmektedir.

## Doldurma İşlemi
Ctrl + Enter : Girilen veriyi seçili hücreye uygular. Birden fazla hücre seçip veri yazdıktan sonra ctrl enter ile seçilen hücerelere doldurma işlemini gerçekleştirir.

Otomatik doldurma özel listelerde de kullanılır. Günler aylar için kayıtlı özel listeler bulunmaktadır. 

Dosya -> seçenekler -> excel seçenekleri -> gelişmiş -> özel listeleri düzenle : yeni liste ekleyip istediğimiz şekilde özel liste oluşturabiliriz.

## Hücre biçimlendir 
Sağ tık hücre biçimleri => sayı ve metin formatları düzenlenebilir (tarih telefon numarası vb.)

Biçim boyacısı : bir güceredeki biçimlendirmeyi alıp başka bir hücreye aktarabilmeye olanak sunar. İlk hücreye basılır biçim boyacısına tıklanır ve yeni veride o biçimi kullanır.

## Çıktı ayarları
Özellikler sayfa düzeni içerisinde sayfa yapısında belirtilebilir.
Üst bilgi, çalışma sayfası vb.
Alt köşedeki sayfa sonu önizleme ile çıktıda görünecek sayfa boyutlarını görüp düzenleyebiliriz.
Üst ve alt bilgi eklenerek çıktıda kağıda görünebilir.

Görünüm sekmesindeki bölmeleri dondur seçeneğinden istenilen satırın ya da sütunun sabit kalmasını sağlayabiliriz. İlk sütunda yazılan verilerin sayfayı kaydırdığımızda sabit kalması (tablo vb. oluşturulduğunda)
Özel dondurma işlemlerinde seçilen hücrenin üst ve sol kısmını dondurur.
Doldurma işleminde hücre biçimini kullanmak istemiyorsak altta çıkan seçeneklerden biçimlendirmeden doldur seçeneğini seçebiliriz.

## Fonksiyonlar
İki nokta aralığı işleme al noktalı virgül aralığı almaz.

Otomatik doldurma için bir hücre sabit kalacaksa hücreyi seçtikten sonra f4 tuşu ile sabit hale getirebiliriz.("$A1$")
Tek taraflı sabitlemelerde satırı ya da sütunu kilitler.
|1|2|3|4|
|-|-|-|-|
|2||||
|3||||
|4||||
|5||||
tablosunu çarpma için kullanacak olursak  => =$A5 * B#1

## Tablolar ve Veri Yönetimi

Veri sekmesinde sırala seçenekleri arasında...
A'dan Z'ye, küçükten büyüğe yeniden eskiye sıralama yapar.
Birden fazla sütunda sıralama yapmak için sırala seçeneğine tıklayıp seçenekler seçilir.

## Alt toplam

Bölgelere göre toplam satışı aramak için, bölgeleri sıraladıktan sonra toplam için alt toplam istenir.

## İç içe eğer
EĞER(A > B; "..."; EĞER(A = B; "..."; "..."))

## Koşullu biçimlendirme
Giriş sekmesindeki Koşullu Biçimlendirme kullanılır. 
Önce alan seçilir. Büyükse ya da küçükse renklendir gibi örnekler için hücre vurgulama kuralları kullanılır.
İlk 10 ya da son 10 öğe, toplam öğelerin ilk yüzde 10u son yüzde 10u gibi seçenekler uygulanabilir.

## Koşullu hesaplama
Belirli kriterlere uygun hesaplamalar yapılacağı zaman kullanılır. 
ETOPLA : Kritere uyduğu durumda topla (şehri Ankara olanların gideri), 
EĞERORTALAMA : Asus marka ürünlerin satış ortalaması, 
EĞERSAY : Asus marka ürünlerin sayısı 
=> case insensitive dir
Kriteri verinin olduğu hücreden referans göstermek ileride hücre sıralaması değiştiğinde sorunlara yol açabilir.

## Yinelenenleri Silme
Veri sekmesinde veri araçlarında yinelenenleri kaldır seçeneğinden sadece birer örnek kalacak şekilde düzenler.

## Çok kriterli fonksiyonlar
Bursa şehrindeki Asus ürünlerinin adet toplamını hesapla gibi sorunlar için =>

ÇOKETOPLA, ÇOKEĞERSAY, ÇOKEĞERORTALAMA fonksiyonları kullanılır.

## Metin fonksiyonları
Veri => Metni sütunlara dönüştür : Belirtilen özelliğe göre yan sütuna taşır (boşluk gördükçe işlemi yap gibi) 
Formüller => Metin => Soldan fonksiyonu : Metnin solundan belirlenen sayıdan karakter alır (adının ilk iki harfi gibi) /Sağdan tam tersi
Formüller => Metin => PARÇAAL : Kaçıncı karakterinden itibaren kaç karakter (substring gibi)
Birleştir : iki metni birleştirir.

## Veri düzenleme
Metni ayırmak için bir ayraç yok ise sabit genişlik seçeneğini kullanarak elle düzenlemeler yapabilmekteyiz. 3er karakter olarak ayır gibi

CTRL + Shift + , : o günün tarihi
CTRL + Shift + . : o anki saat

Tip dönüşümü için de metni sütunlara çevir kullanılabilir. ay/gün/yıl şeklinde gelen tarihi sistem tarihine çevirmek için...

metni parçalama, büyük harfe çevirme gibi seçenekler için ilk örneği yazıp hızlı doldurduğumuzda otomatik olarak işlemi gerçekleştirecektir. 

## Arama ve Başvuru
Düşey ara : farklı tablolardan verileri karşılaştırarak, alınmak istenen veriyi getirir.
Aynı ya da farklı sayfa ya da kitaplarda kullanılabilir.
İki tabloya ihtiyaç vardır : yerleştirilmek istenilen yer, verinin alınacağı yer.
Aranan değer, aranan yer, alınmak istenilen veri kaçıncı sırada...

- Veriyi yerleştireceğin tablodan seçilir
- Aranacak yer taranır (ortak alan başta kalmalı)
- kaçıncı sütunda kaldığı yer olarak verilir
- aralık bak 1/0 => tam eşleşme = 0

- değer 1 olursa yaklaşık eşleşme anlamına gelir. Sayısal aralıklara bakılıyorsa, if else anlamına gelen bir yapıda arama yapar.
- Arama yapılan tablo küçükten büyüğe sıralanması gerekmektedir. Tablo aralağında olmayan bir değer olduğunda #YOK gelebilir.
Yoktan kaçınmak için EĞERHATA fonksiyonu çalıştırılabilir.

- Hep ortak alanın sağından veri alabilir ve sürekli tarama yapmak zorunda olmamız performans kaybına neden olur.

Düşey ara mantığı : yukarıdan aşağı aramaya başlar bulduğunda sağa doğru devam eder.

## Kaçıncı Fonksiyonu
- Aranan değer
- Aranan dizi
- eşleştir => 0 : birebir

aradığım verinin olduğu sütunu taramam yeterli 
=> sonuç olarak kaçıncı sırada olduğunu gösteir

## İndis Fonksiyonu
Kaçıncıdan aldığımız parametreyi gödererek seçilen sütundan o satırdaki işlemi gönderir

## Tarihsel Fonksiyonlar
- YIL(tarih) 
- Ay(tarih)
- GÜN(tarih)
- HAFTANINGÜNÜ(tarih, hafta hangi günle başlıyor) : ptesi için 2 => o hafta içinde kaçıncı gün 
- HAFTASAY(tarih) : o yıl içindeki kaçıncı haftada
- BUGÜN()
- Ctrl + shift + , : bugünün tarihi
- Ctrl + shift + . : şuanın tarihi
- METNEÇEVİR(tarih, "gggg")

## GRAFİKLER

Sayısal verileri görsel hale getirmemizi sağlayan yapılar.

### Sütun Grafiği
Ekle sekmesinden geçilir.

- Kategori listesi : x ekseni
- Değerler listesi : y ekseni
- Arka plan çizim alanıdır.

Kaldırılan öğeler Grafik Öğesi Ekle seçeneğinde bulunurlar

### Çizgi Grafiği
Zamana bağlı değişimi göstermek için kullanırız. Tarihsel bir veriye ihtiyaç duyulur. Verinin tarihe bağlı dağılımını görmek için kullanırız.

Trendin yönünü görebilmek için eğim çizgileri eklenebilir.

### Pasta Grafiği
Yüzdesel oran görmek için kullanılır.
2d, 3d ya da halka olarak kullanılabilir.

### Birleşik Grafik
Sütun grafiklerinde değerlerden birinin çok küçük ya da çok büyük aralıkta olması durumunda üzerinde bir eksen daha seçilip üzerinde çizgi grafiği oluşturulur.

### Harita Grafiği
Ülke ve il bilgileri için harita üzerinden görselleştirme sağlar. İnternete bağlı olmak gerekmektedir.

### Mini Grafik
Farklı bilgiler için karşılaştırmak için kullanılabiliecek belirli veri aralığını belirli hücrelere grafik olarak yerleştirir.

## Veri Doğrulama 
Ortak alanda olan dosyanın farklı kişiler için kullanımını kısıtlayan yapı doğrulamadır.
Hücrelere gelecek olan verileri belirlemek de veri doğruluğudur

Korunma : 
 - Dosyanın korunması : dosyayı şifreleme => dosya sekmesi - bilgi ekranı - çalışma kitabını koru (girişte şifre isteyecek)
 - Sayfanın korunması : dosyayı açar inceler ancak veriler üzerinde değişiklik yapamaz -> çalışma kitabının üzerinden sayfayı koru / gözden geçir koruma sayfayı koru
 - Hücrenin korunması : Kullanıcının bazı hücrelere veri girebileceği ancak bazılarında değişiklik yapmasını engelleyebilecek bir oluşturmak. -> seç hücreleri biçimlendir koruma 

Doğrulama :
 - Kullanıcının gireceği verinin şeklini kısıtlama
 Aralığı seç veri doğrulamaya gir. İzin verilen değeri tanımla
 
## Pivot Tablo
 Analizler için kullanılır, özet gösterimini kolaylaştırır.
 Ekle Sekmesinden oluşturulur.
 
 - Birleştirilmiş hücreler engel olur.
 - Tablo başlıklarından herhangi birinin eksik olmaması gerekmektedir.
 - Satır ve sütuna görülmek istenen öğeler eklenir. Analizler için de Değerler kısmı kullanılır.

## Makrolar 
Excel'in yazılım tarafı..
Düzenli olarak yapılması gereken raporlar, sürekli hesap yapılıp güncellenen veriler makrolar ile yapılır.

- Geliştirici sekmesinin açılması gerekmektedir. => Dosya - seçenekler - Şeridi özelleştir - Geliştirici
- İki çeşittir : Kayıt makrosu - Kod makrosu
- Visual Basic programlama dili ile işlemleri gerçekleştirir.
- Bütün office uygulamalarında kullanılır : outlook üzerinden otomatik mailler, exceldeki tabloyu powerpoint sunumuna eklemek gibi 

### Makro Kaydetmek
- Makro adı ve yer belirtilir.
- Açıklaması yazılabilir.
- Kişisel makro Çalışma Kitabı : diğer excellerde de kullanılacak şekilde kaydolur.

### Makro Koduna Müdahele Etmek
- Komutlar visual basic ekranında modüllerin altında bulunur.
- makro kaydedip kodu almak ya da kodu değiştirmek mümkündür.
- Makrolu dosyaların uzantısı .xlsm dir, farklı kaydet(f12) diyerek kaydetmemiz gerekmektedir. => Makro içerebilen Excel kitabı

Geliştiricilerden ekle diyerek buton ekleyebilir ve butona basıldığında istenilen makroyu çalıştırabiliriz.

### Göreceli başvuru
Genelde verilerin üst üste yazılmasını engellemek için yapılan işlemlerdendir.
