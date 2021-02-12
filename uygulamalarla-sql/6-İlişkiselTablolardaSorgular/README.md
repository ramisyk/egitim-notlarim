# 6 - İlişkisel Tablolarda Sorgular

**Eğitim için başlangıçta:**
Countries, Cities, Towns, Districts, Address, Users tabloları hazırlanmış ve örnek verilerle doldurulmuştur.

## İki Tabloyu Birleştirme
`
SELECT * FROM USERS WHERE ID = 1 
SELECT * FROM ADDRESS WHERE USERID = 1
`
![İkiTablo](https://github.com/ramisyk/egitim-notlarim/blob/master/uygulamalarla-sql/6-%C4%B0li%C5%9FkiselTablolardaSorgular/kaynak/1_IkiTablo.png "Aynı ID'de İki Farklı Tablo Sonucu")
Yukarıdaki sonucu tek tabloda (USERID = 1 iken kullanıcı bilgileri ve addres i gösteren tablo) aşağıdaki şekilde oluşturulur:
`
SELECT USERS.*, ADDRESS.ADDRESSTEXT FROM
USERS, ADDRESS
WHERE USERS.ID=ADDRESS.USERID
AND USERS.ID=1
`
![İkiVeriTekTablo](https://github.com/ramisyk/egitim-notlarim/blob/master/uygulamalarla-sql/6-%C4%B0li%C5%9FkiselTablolardaSorgular/kaynak/2_IkiVeriTekTablo.png "İki Farklı Tablodan Getirilen Veriler")

## Alias Kullanımı
`
SELECT 
USERS.NAMESURNAME, USERS.EMAIL, USERS.GENDER, USERS.BIRTHDATE,
ADDRESS.ADDRESSTEXT 
FROM USERS, ADDRESS
WHERE USERS.ID=ADDRESS.USERID
AND USERS.ID=1
`
Yukarıdaki sorguda her yerde users ve address isimlerini kullanmak sorgunun okunurluluğunu kötü bir hale getiriyor. Bunun yerine users yerine sadece u harfini address yerine de sadece a harfini kullanarak sorgudaki karmaşık görünümün önüne geçebiliriz. =>
`
SELECT 
U.NAMESURNAME, U.EMAIL, U.GENDER, U.BIRTHDATE,
A.ADDRESSTEXT 
FROM USERS U, ADDRESS A
WHERE U.ID=A.USERID
AND U.ID=1
`

Çok daha fazla tablodan sorgu yapılması durumunda bu yapı daha kullanışlı bir hale getirebilir. 

Select kısmındaki kolon isimlerinden sonra yazılacak kelimeler de o kolon için allias niteliği taşımaktadır.

## İkiden Fazla Tablo Kullanımı
Hazırladığımız veritabanında tablolardan kullanıcı bilgilerinin yanına, açık adres, semt, ilçe, il, ülke isimlerinin bilgilerini de vemek istediğimiz durumda Users, Address, Districts, Towns, Cities, Countries tablolarının tümünü kullanmamaız gerekmektedir.
**Not:** Address tablosunda DistrictsId, TownId, CityId bilgileri bulunmaktadır ve Cities tablosunda CountryId bilgisi bulunmaktadır. Bu bilgiler sayesinde isim bilgilerine ulaşılacaktır. 

`
SELECT 
U.NAMESURNAME AdSoyad, 
U.EMAIL e_mail,
U.GENDER Cinsiyet, 
U.BIRTHDATE DogumTarihi,
A.ADDRESSTEXT AcikAdres,
D.DISTRICT Semt,
T.TOWN Ilce,
CT.CITY Sehir,
C.COUNTRY Ulke
FROM USERS U, ADDRESS A, CITIES CT, COUNTRIES C, TOWNS T, DISTRICTS D
WHERE U.ID = A.USERID AND 
	  D.ID = A.DISTRICTID AND
	  T.ID = A.TOWNID AND
      CT.ID = A.CITYID AND 
	  C.ID = CT.COUNTRYID
      AND U.ID=1
`
![IkidenFazlaTablo](https://github.com/ramisyk/egitim-notlarim/blob/master/uygulamalarla-sql/6-%C4%B0li%C5%9FkiselTablolardaSorgular/kaynak/3_IkidenFazlaTablo.png "İkiden Fazla Tablo Kullanımı")
## İlişkisel Tablolarda Aggregate Fonksiyonlar
**Kişilerin adres sayısı**
`
SELECT 
U.NAMESURNAME,COUNT(A.ID) AS ADRESSAYISI
FROM USERS U, ADDRESS A, COUNTRIES C, CITIES CT, TOWNS T, DISTRICTS D
WHERE U.ID = A.USERID AND
C.ID = A.COUNTRYID AND
CT.ID = A.CITYID AND 
T.ID = A.TOWNID AND
D.ID = A.DISTRICTID
GROUP BY U.NAMESURNAME
`
![Aggregate](https://github.com/ramisyk/egitim-notlarim/blob/master/uygulamalarla-sql/6-%C4%B0li%C5%9FkiselTablolardaSorgular/kaynak/4_Aggregate.png "İsme göre adres sayısının görüntülenmesi")

## Join İşlemleri
`
SELECT 
A.KolonAdi1, A.KolonAdi2, B.KolonAdi3, B.KolonAdi4
FROM Tablo1 A
JOIN Tablo2 B ON A.PK = B.FK
`
**JOIN kullanım örneği:**
`
SELECT U.NAMESURNAME, U.EMAIL,
A.ADDRESSTEXT, C.COUNTRY, CT.CITY,
T.TOWN, D.DISTRICT
FROM USERS U
JOIN ADDRESS A ON A.USERID = U.ID
JOIN COUNTRIES C ON C.ID = A.COUNTRYID
JOIN CITIES CT ON CT.ID = A.CITYID
JOIN TOWNS T ON T.ID = A.TOWNID
JOIN DISTRICTS D ON D.ID = A.DISTRICTID
`

![Join](https://github.com/ramisyk/egitim-notlarim/blob/master/uygulamalarla-sql/6-%C4%B0li%C5%9FkiselTablolardaSorgular/kaynak/5_Join.png "Join Sorugu Sonucu")

Join fonksiyonu ile birleştirilecek tablo primary key ve foreign key ilişkisi göz önünde bulundurularak eklenir. Birleşme koşulu ON anahtar kelimesi ile gösterilir.

**JOIN ve Aggregate fonksiyonların kullanımı:**
Şehirlere göre kullanıcı sayısının JOIN ile belirlenmiş hali:

`
SELECT 
CT.CITY, COUNT(U.ID) AS KullaniciSayisi
FROM USERS U
JOIN ADDRESS A ON A.USERID = U.ID
JOIN CITIES CT ON CT.ID = A.CITYID
GROUP BY CT.CITY
`

![JoinAggregate](https://github.com/ramisyk/egitim-notlarim/blob/master/uygulamalarla-sql/6-%C4%B0li%C5%9FkiselTablolardaSorgular/kaynak/6_JoinAggregate.png "Join ile Aggregate")

### Inner Join
Küme kesişimi gibi çalışır. İki tabloda ortak olan kayıtları getirir. Yalnızca join kullanılması inner join kullanımıdır.

![InnerJoin](https://github.com/ramisyk/egitim-notlarim/blob/master/uygulamalarla-sql/6-%C4%B0li%C5%9FkiselTablolardaSorgular/kaynak/7_InnerJoin.png "Inner Join Tablo Örneği")

### Left (Outer) Join
Inner join gibi kesişimler tek sütun haline gelir ancak, sol tablo için sağ tabloda veri olmasa daki sol tablonun bütün elemanları join tablosunda bulunur karşılığı boş bırakılır.
Aşağıdaki örnekte Alper'e ait bir adres bilgisi olmamasına rağmen join tablomuzda bulunmaktadır.

![LeftJoin](https://github.com/ramisyk/egitim-notlarim/blob/master/uygulamalarla-sql/6-%C4%B0li%C5%9FkiselTablolardaSorgular/kaynak/8_LeftJoin.png "Left Join Tablo Örneği")

### Right (Outer) Join
Left Join in tam tersidir. Sağdaki tablo referans alınarak doldurulur. Sağdaki tabloda bulunup soldaki tabloda da ortak olan veriler ortak şekilde eklenirken sağda olmasına rağmen solda yoksa o kolonlar boş bırakılarak sağ tablodan ekleme yapılmaya devam edilir. Solda olduğu halde sağ tabloda bir referansı yoksa join tabloısuna eklenmez.

![RightJoin](https://github.com/ramisyk/egitim-notlarim/blob/master/uygulamalarla-sql/6-%C4%B0li%C5%9FkiselTablolardaSorgular/kaynak/9_RightJoin.png "Right Join Tablo Örneği")

### Full Join
İki tablodaki verilerin tümünün join tablosuna eklenmesidir. Ortak veriler ortak şekilde gelirken, ortak olamayan verilerin karışları boş bırakılarak tabloya eklenir.

![FullJoin](https://github.com/ramisyk/egitim-notlarim/blob/master/uygulamalarla-sql/6-%C4%B0li%C5%9FkiselTablolardaSorgular/kaynak/10_FullJoinTable.png "Full Join Tablo Örneği")

Tabloların herhangibirinde karşılığı olmayan verilerin de join tablosunda görünebilmesi ilk örnekler yerine **join kullanımının avantajıdır.** 

## Sorular
- İlişkisel veritabanında birden fazla tablo birleştirme
- JOIN nedir?
- Join türleri nelerdir nasıl çalışır?
- Master Detay tablolar nasıl bağlanarak sorgu yapılır?
- ALIAS nedir?
- JOIN ve ALIAS
- JOIN ve GROUP BY