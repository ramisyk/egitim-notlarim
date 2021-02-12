# 4 - Veri Tipleri

Veri tabanı oluşturulurken, veri tiplerini kullanılacak veriye uygun olarak belirlemeliyiz. Metin, sayısal, tarih şeklinde veri tiplerini doğru olarak tanımlamalıyız ve yer kaplama, performans gibi sorunlarla karşılaşma ihtimalimizi düşürmeliyiz. Veri tabanında veri tiplerinin belirlenmesi ve doğru kullanılması *normalizasyon* işlemidir.

## Tam Sayılar
| Veri tipi   | Minimum Değeri                     | Maksimum Değeri                    | Boyutu    |
| ----------- | ---------------------------------- |------------------------------------|-----------|
| bigint      | -2^63 (-9,223,372,036,854,775,808) | 2^63-1 (9,223,372,036,854,775,807) | 8 Byte    |
| int         | -2^31 (-2,147,483,648)             | 2^31-1 (2,147,483,647)             | 4 Byte    |
| smallint    | -2^15 (-32,768)                    | 2^15-1 (32,767)                    | 2 Byte    |
| tinyint     | 0                                  | 255                                | 1 Byte    |
| bit         | 0                                  | 1                                  | <=8 1 Byte|

## Ondalıklı Sayılar
![ondalikliSayilar](https://github.com/ramisyk/egitim-notlarim/uygulamalarla-sql/blob/master/4-VeriTipleri/kaynak/ondalikSayilar.png "Ondalıklı Sayılar Tablosu")

## Metin Veri Tipleri
- char(50)
- nchar(50)
- ntext
- nvarchar(50)
- nvarchar(MAX)
- text
- varchar(50)
- varchar(MAX)

char ve nchar için parantez içlerinde belirtilen kadar yer ayrılır ve kayıt uzunluğu ne kadar olursa olsun ayrılan yer kadar kullanılır; örneğin 50 karakterli bir char ya da nchar için 5 karakterlik bir isim kaydolursa ismin sonuna 45 karakterlik boşluk bırakılır. Ve her karakterde 1 Byte yer kaplar.

Diğer metin değişkenlerinde maximum alınacak değer belli olsa da içinde alınan kayıt kadar yer kaplar.

char tipinin uzunluğun sabit tutulması ve uzunluğu bilinen değişkenlerde arama yapmanın daha kolay olacağı durumlarda kullanılması daha avantajlıdır (T.C. kimlik no). Diğer veri tiplerinde öncelikle uzunluk hesaplaması yapılması gerekmektedir.

char, varchar, text tiplerinde uluslararası semboller yer almamaktadır. Çince ya da Arapça'daki harf sembollerini içermemektedir, bu nedenle tanımlama yapamaktadır. Bu tip kelimeler için nchar, nvarchar ya da ntext kullanılmalıdır.
char ve varchar her karakter için 1 Byte yer kaplarken başına "n" gelenler 2 Byte yer kaplar.

metin veri tipleri sütun 8000 byte ı geçmemeli;
- char => max 8000 karakter
- nchar => max 4000 karakter

varchar(MAX) => 2 gb ye kadar veri tutabilir.
text => eski SQL sürümlerinde / artık kullanılmamaktadır uyumluluk için bulunmaktadır.

## Tarih ve Saat Veri Tipleri
![tarihSaat](https://github.com/ramisyk/egitim-notlarim/uygulamalarla-sql/blob/master/4-VeriTipleri/kaynak/tarihSaat.png "Tarih ve Saat Veri Tipleri Tablosu")
- date: sadece tarih
- datetime: tarih ve saat
- datetime2: milisaniye hassasiyeti
- datetimeoffset: ek olarak timezone tutulur
- time: sadece saat milisaniyeden sonra 4 digit

## Diğer Veri Tipleri
![diger1](https://github.com/ramisyk/egitim-notlarim/uygulamalarla-sql/blob/master/4-VeriTipleri/kaynak/diger1.png "Diğer Veri Tipleri Tablosu")
![diger2](https://github.com/ramisyk/egitim-notlarim/uygulamalarla-sql/blob/master/4-VeriTipleri/kaynak/diger2.png "Diğer Veri Tipleri Tablosu")
- image: eski SQL versiyonlarında resim dosyaları için kullanılır
- binary: doğrudan okunamaz çevirici gerektirir.
- varbinary(MAX): dosyanın kendisi veritabanında saklanıyorsa kullanılır
- xml: xml türünde string veri, sorgulanabilir bir veri olarak tutulur.
- uniqueidentifier: sadce kendi tablomda global olarak eşsiz bir veri tutmak için (örn. IOT verileri)
- hierarchyid: hiyerarşileri tutmak için (çalışan müdür pozisyonları)

## Sorular
- Veri Tipi Kavramı nedir?
- Sayısal Veriler nelerdir?
- Integer, SmallInt, BigInt, TinyInt Farkları?
- Float, Decimal, Money ?
- Varchar, char, nchar, nvarchar ?
- date, time, datetime ?
- Hangi tip ne kadar hafiza tutar?
- Hangisini neye göre seçeriz?