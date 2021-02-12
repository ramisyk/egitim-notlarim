# 2 - Temel SQL Komutları

## Data Manipülasyon Komutları

- SELECT : Tablolardan kayıt çeker
- UPDATE : Kayıtların belirli alanlarını günceller
- DELETE : Bir tablodan kayıt siler
- INSERT : Tabloya yeni kayıt ekler
- TRUNCATE : Tablonun içini boşaltır

DELETE vs. TRUNCATE
DELETE komutunda belirli alanları, tabloda bulunan şartları sağlayan kayıtları (yaşı 15'ten büyük olan herkes gibi) silebilirken TRUNCATE herhangi bir koşula bakmaksızın tabloyu tamamen temizler ve ilk haline getirir.

## Veritabanı Manipülasyon Komutları

- CREATE DATABASE : Yeni veritanabı oluşturur.
- ALTER DATABASE : Veritabanının özelliklerini değiştirir.
- CREATE TABLE : Yeni tablo oluşturur.
- ALTER TABLE : Tablonun özelliklerini değiştirir.
- DROP TABLE : Tabloyu tamamen siler
- CREATE INDEX : Index oluşturur
- DROP INDEX : Index siler

## SELECT Komutu
Veri çekmeye yarayan komut 

`SELECT kolonAdi1, kolonAdi2,... FROM tabloAdi` 
SELECT komutundan sonra istenilen sütun adları yazılır - tüm sütunlar isteniyorsa "*" kullanılır - sonrasında FROM anahtar kelimesi kullanılır ve sütunların istendiği tablonun ismi yazılır.

## INSERT Komutu
Tabloya kayıt eklemek için kullanılır

`INSERT INTO TabloAdi (kolonAdi1, kolonAdi2,...)
 VALUES (deger1, deger2,...)`
 
INSERT komutu INTO ile birlikte kullanılır ve sonrasında ekleme yapılacak olan tablonun adı yazılır. Parantez içinde sütun isimleri eklendikten sonra VALUES anahtar kelimesi eklenir ve parantez içinde sırasıyla sütunlara karşılık gelecek değerler yazılır.
String değerler için 'tek tırnak' kullanılır.
 
## UPDATE Komutu
Var olan bir kaydın güncellenmesi ya da değiştirilmesi için kullanılır.

`UPDATE TabloAdi
 SET kolonAdi1=deger1, kolonAdi2=deger2
 WHERE <şart komutları>`
 
 UPDATE komutundan sonra  güncelleme yapılmak istenilen tablonun adı yazılır. SET komutu eklenir ve sonuna değişiklik yapılacak sütun adları ve değerleri yazılır. WHERE komutu ile de hangi koşulllarda değişiklik yapılmak istendiği belirtilir.
 Şart eklenmemesi durumunda o sütuna ait tabloda bulunan bütün veriler güncellenir
 ## DELETE Komutu
İstenilen tablodan kayıt silmek için kullanılır
`DELETE
 FROM TabloAdi
 WHERE <Şartlar>`
 
 DELETE komutundan sonra tablo ismi eklenir ve hangi şartlarda silme yapılacağını belirterek işlem tamamlanır.
 Şart eklenmemesi durumunda tablodaki bütün kayıtlar silinir.
 
 ## TRUNCATE Komutu
Tabloyu sıfırdan oluşturulmuş haline getirir.
Otomatik artan yapı varsa, delete komutundan sonra baştan başlamaz kaldığı yerden devam eder ancak truncate tabloyu ilk haline getirir.
TRUNCATE daha hızlı çalışan bir komuttur.

## WHERE Kavramı
Veri ekleme, silme, seçme işlemlerinde istenilen kriterlere uygun verileri almak için kullanılır.
`WHERE city = 'Bursa'`

## AND ve OR Operatörleri
WHERE komutuna birden fazla şart vermek için kullanılır.
AND kullanımında iki şartı birden karşılaması gerekirken OR için birinin doğru olması yeterlidir.

## DISTINCT Komutu
Verilen sütındaki tekrar eden değeler içinden sadece bir tanesini getirir.

## ORDER BY Komutu
Sıralama yapmak amacıyla kullanılır. 
`SELECT kolonAdi1, kolonAdi2,...
 FROM TabloAdi
 ORDER BY kolonAdi1 ASC, kolonAdi2 DESC`

Seçim yapılmak istenilen sütunlar belirtildikten sonra gelen verinin hangi sütunlara bağlı olarak sıralandırılacağı ORDER BY ile belirtilir. ASC küçükten büyüğe, DESC büyükten küçüğe sıralama yapar. Hiç bir şey yazılmamışsa ASC olarak sıralama yapar.
ORDER BY 5, 2 => 5. ve 2. sütunlara göre sıralama yap.

## TOP Komutu
Veri setinden dönen kayıtların tamamını görmek yerine belirtilen kısmını görmeye yarar.
`SELECT TOP N
 kolonAdi1, kolonAdi2,...
 FROM TabloAdi`
N yerine görülmek istenilenler gönderilir. TOP 100 ilk 100 kayıt, TOP 50 PERCENT kayıtların yüzde ellisi....

## SORULAR
- SQL Komutları nelerdir? 
- DMS ve DBMS ? 
- Truncate vs. Delete
- DISTINCT
- TOP