# 3 - SQL Komutları

## Aggregate Functions

SUM, MIN, MAX, AVG, COUNT fonksiyonları
`SELECT 
 SUM(PRICE), COUNT(ID), MIN(PRICE), MAX(PRICE), AVG(PRICE)
 FROM Tablo`

- SUM : Sütundaki değerlerin toplamı.
- COUNT : Sütundaki eleman sayısı.
- MIN : Belirtilen sütundaki en **küçük** değer (int, date, string olabilir)
- MAX : Belirtilen sütundaki en **büyük** değer
- AVG : Belirtilen sütunun ortalaması.

Satış bilgisi tutan bir mağaza için örnek sorgular:

`SELECT * FROM SALES`

`SELECT COUNT(*) FROM SALES`

`SELECT MIN(AMOUNT),MAX(AMOUNT), COUNT(FICHENO), SUM(AMOUNT), AVG(AMOUNT) FROM SALES`

`SELECT MIN(TOTALPRICE), MAX(TOTALPRICE), COUNT(FICHENO), SUM(TOTALPRICE), AVG(TOTALPRICE) FROM SALES`

`SELECT MIN(TOTALPRICE), MAX(TOTALPRICE), COUNT(FICHENO), SUM(TOTALPRICE), AVG(TOTALPRICE) FROM SALES
WHERE CITY = 'ANKARA'`

`SELECT MIN(TOTALPRICE), MAX(TOTALPRICE), COUNT(FICHENO), SUM(TOTALPRICE), AVG(TOTALPRICE) FROM SALES
WHERE CITY = 'İSTANBUL'`


## GROUP BY Komutu
Aggregate fonksiyonları GROUP BY ile kullanmak daha anlamlı yapılar elde etmemizi sağlayabilir. Toplam satışı ay, yıl ya da şehirlere göre gruplandırarak listelemek analiz yapmak için daha kullanışlı bir geri dönüş sağlar.

Örnek sorgular:

**Şehire göre gruplandırma yaparak kazanç durumlarını listelemek.**

`SELECT CITY,
 MIN(TOTALPRICE) AS MINPRICE, 
 MAX(TOTALPRICE) AS MAXPRICE, 
 COUNT(FICHENO) AS ROWCOUNT_, 
 SUM(TOTALPRICE) AS TOTALPRICE, 
 AVG(TOTALPRICE) AS AVGPRICE
 FROM SALES
 GROUP BY CITY
 ORDER BY CITY `

**Gün bazlı satış rakamları**
`SELECT CITY, DATE2, SUM(TOTALPRICE) AS TOTALPRICE, COUNT(FICHENO)
FROM SALES 
WHERE CITY = 'ANKARA'
GROUP BY CITY, DATE2
ORDER BY CITY, DATE2 `

**Bir günün şehir bazlı satış rakamı**
`SELECT DATE2, CITY, SUM(TOTALPRICE) AS TOTALPRICE
FROM SALES
WHERE DATE2 = '2019-01-02'
GROUP BY DATE2, CITY
ORDER BY DATE2, SUM(TOTALPRICE) DESC`

## Sorular
- DB nasıl restore edilir?
- Aggregate fonksiyonlar nelerdir, neden nasıl kullanılırlar?
- Group By nasıl nasıl kullanılır?
- Having komutu nasıl kullanılır?
