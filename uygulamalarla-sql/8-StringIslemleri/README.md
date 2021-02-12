# 8 - String İşlemleri

SQL Server üzerinde SQL komutları dışında T-SQL kodları ile de bir çok string işlemi yapılabilmektedir.
## ASCII
Fonksiyonun içinin ASCII türünden değerini verir.
SELECT ASCII('A') => 65

## CHAR
Fonksiyonun içindeki ASCII değerinin karakter sonucunu gönderir.
SELECT CHAR(65) => A

## SUBSTING
Verilen metnin kaçıncı karakterinden başlayarak kaç karakterlik bir metin oluşturulacağı bilgisi verilerek çalışır.
SELECT SUBSTRING('RAMİS YÜKSEL', 7, 6) => YÜKSEL

SELECT * FROM USER_ WHERE SUBSTRING(USERNAME_, LEN(USERNAME_), 1) = 'A' : Son karakteri A olanları getir.

## CHARINDEX
SELECT CHARINDEX('Y', 'RAMİS YÜKSEL', 1) => 7 : 1. karakterden aranmaya başlandığında Y kaçıncı karakterdir.

## CONCAT
İki veya daha fazla stringin yan yana yazılması

SELECT CONCAT('Ramis', ' ', 'Yüksel') => Ramis Yüksel
SELECT CONCAT_WS(' ', 'Ramis', 'Yüksel') => Ramis Yüksel

Girilen stringler arasına bir ayırıcı eklenmek istendiğinde concat de karışık bir görüntü olabiliyor. Bunun için CONCAT_WS nin ilk elemanında seperator belirlenir ve stringler yan yana eklenir

## FORMAT
Sayı ya da tarih türündeki değerleri istenilen türde yazılmasını sağlar

SELECT FORMAT(GETDATE(), 'd', 'en-us') => 02/09/2021  (ay/gün/yıl)
SELECT FORMAT(GETDATE(), 'D', 'en-us') => Tuesday, February 9, 2020

## LEFT, RIGHT, LEN
Soldan ya da sağdan istenilen kadar karakter alınmasını sağlar
SELECT LEFT('RAMİS YÜKSEL', 5) => RAMİS
SELECT RIGHT('RAMİS YÜKSEL', 6) => YÜKSEL
SELECT LEN('RAMİS YÜKSEL') => 12 : Metinin karakter sayısını verir
## TRIM, LTRIM, RTRIM
TRIM: Baş ve sondaki boşlukları temizler
LTRIM: Sadece baştaki boşlukları temizler
RTRIM: Sadece sondaki boşlukları temizler

## LOWER, UPPER
Gönderilen parametredeki tüm karakterleri küçük ya da büyük harfe çevirir.

## REVERSE
Girilen metni tersten yazdırır.

## REPLICATE
Metin ve bir tam sayı değeri alır. Girilen metni verilen sayı kadar yazdırır. 
SELECT REPLICATE('A', 5) => AAAAA

## REPLACE
Metin içerisinde verilen belirtilen bir parçanın, farklı bir parça ile değiştirilmesi.
SELECT REPLACE('KEMAL ATATÜRK','KEMAL', 'MUSTAFA KEMAL') => MUSTAFA KEMAL ATATÜRK