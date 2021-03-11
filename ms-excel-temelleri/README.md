# Microsoft Excel Temelleri

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
Metni ayırmak için bir atraç yok ise sabit genişlik seçeneğini kullanarak elle düzenlemeler yapabilmekteyiz. 3er karakter olarak ayır gibi

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