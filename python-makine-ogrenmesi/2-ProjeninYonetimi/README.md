# Veri Ön İşleme

## Veri Kaynağı
Makine öğrenmesi projesi hazırlık aşamasında kullanılacak verinin elde edilmesi gerekmetedir.

## Kütüphanelerin Yüklenmesi
Kütüphaneler "import" komutu ile eklenir. Genelde okunurluluğun arttırılması için en üste bırakılır.

## Python ve OOP

## Eksik Veriler
Veri setinde eksik olan veriler, verinin durumuna göre doldurulur. Tüm verilere belirtilen bir değer atanabilir ya da ortalama değer ile doldurulabilir. 

## Veri Tipleri
**Kategorik veriler:**

Ordinal, sıraya sokulabilen ancak ölçülemeyen değerler. Plaka numaraları arasında sıra vardır ancak herhangi bir ölçü belirtmez.
Nominal, kategorilendirilebilir ancak sıraya sokulamayan değerler. Araba markaları...

**Sayısal veriler:**
Oransal, birbirine orantılanabilecek değerler. yaş gibi ?
Aralık, ?

Sayısal değer olmayanların, bir şekilde sayısal değerlere dönüşmesi gerekmektedir. Cinsiyet tablosu sayısal değerlere dönüşürken kadınlara 1 erkeklere 0 değerleri atandığında sorunsuz dönüşüm olabilmektedir. Ancak Türkiye, Amerika, Fransa nın olduğu ülke sütununda ülkelere sıra ile değer vermek bizi doğru sonuca ulaştırmaz. Bu durumda her ülke sütun haline getirilir ve geçerli ülkenin olduğu satırda o ülkeye 1 diğer durumlarda 0 değeri atanır. 