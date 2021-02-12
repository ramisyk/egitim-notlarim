# 5 - İlişkisel Veri Tabanı
Birden fazla tablonun bir arada kullanılması ile oluşur. Temel amaç tekrar eden verileri minimuma indirmektir.  
## İlişkisel Veri Tabanı Tasarımı
**E-Ticaret Sitesi Veri Tabanı Örneği:**
- Kullanıcı bilgileri içerek users tablosu olmalı
- Kullancıların birden fazla adresi olacağından **kullanıcı id si ile ilişkilendirilmiş** bir adres tablosu olmalı (foreign key)

Foreign key belirtilirken design table bölümünde add relationships seçeneğinden hangi alanların bağlanılacağı belirtilir.

![iliskiselVeriTabanı](https://github.com/ramisyk/uygulamalarla-sql/blob/master/5-%C4%B0li%C5%9FkiselVeriTaban%C4%B1/kaynak/city-country-relationship.png "İlişki Ekleme")

Tablolar arasında ilişki yapıldığında örn;
country tablosunun id değeri ile city tablosunun countryId değeri arasında bağlantı kurduğumuzda: 
- INSERT ve DELETE işlemlerinde default durumda bırakıldığında:  
    Eğer bir ülkeyi referans olarak kullanan bir şehir varsa country tablosundan silme işlemine onay vermez. Öncelikle şehirlerden o ülkeyi referans gösteren verilerin silinmesini bekler
- INSERT ve DELETE işlemlerinde **Cascade** seçeneği aktif olduğunda:
    Şehirler tablosundan, silinmek istenen ülkeyi referans gösteren bütün şehirleri siler sonrasında da ülkeyi siler.
    Veri tabanında istenmedik bir duruma yol açabilir, önerilmez!
- INSERT ve DELETE işlemlerinde **Set Null** seçeneği aktif olduğunda:
    Ülkeyi siler, o ülkeyi referans gösteren şehirlerin ülke bilgisini *NULL* durumuna getirir, geçmiş bilgisini göstermez.
- INSERT ve DELETE işlemlerinde **Set Default** seçeneği aktif olduğunda:
    Ülkeyi siler, o ülkeyi referans gösteren şehirlerin ülke bilgisini *NULL* durumuna getirir, istenilirse bir değişken atanabilir.

## Sorular
- RDMS Nedir?
- RDMS yapısı nasıl çalışır?
- E-ticaret sistemi nasıl çalışır?
- RDMS veri tabanı mimarisi nasıl oluşturulur