# 1 - Algoritma

# Algoritma Nedir?

Problem çözümünde takip edilmesi gereken yolların tamamı. Kullanılacak komut dizisi.

Algoritma, çözüm için her durumda kararsız kalmadan en kısa yoldan, en az maliyetle hazırlanmalıdır.

Algoritma tasarlamak için problemi iyi anlamalı sade bir biçimde ifade edilebilmelidir.

# Algoritmaların Özellikleri

- Algoritmaların başlangıç ve bitiş noktası olmak zorundadır. Algoritmalar için sonlu adımlar kümesinden oluştuğunu söyleyebiliriz.
- Algoritma tasarımı yapılırken sade ve anlaşılır bir biçim kullanılmalıdır, inceleyenlerin anlayacağı şekilde olmalıdır bu nedenle teknik söylemlerden mümkün olduğunca arındırılmış olmalıdır.
- Algoritma her durum için cevap vermek zorundadır, kararsız kalma durumu söz konusu olamaz.
- Maliyeti en az olan yol seçilmelidir.
- Algoritmanın verimli olması için kullanılacak donanım kaynakları dikkate alınmalı, belirlenen alan ve zaman içerisinde problemin çözümü hazırlanmalıdır.
- Başlangıç koşullarının ve giriş değerlerinin belirtilmesi algoritma verimini arttırır.

# Algoritmaların Matematikteki Yeri

- Algoritmalar aritmetik ve mantıksal işlemler içerebilirler.
- Algoritmalar, matematiksel olarak prosedür ya da fonksiyon olarak düşünülebilir.
- Karşılaştırma ve mantık işlemlerini kod üzerinde kullanabiliriz.
- Belirli durumlarda giriş değeri olan fonksiyonlarda çıkış değeri olması gerekebilir.
- Günlük hayatta algoritmaların çözüm sunduğu karmaşık durumlarda, probleme uygun olarak çok fazla veri bulunabilmektedir ve çözüm için bilgi toplamak ve toplanan bilgilerin doğruluğunu onaylatmak gerekebilir. Toplanan veri üzerinden problemi öğrenmeye çalışabiliriz.
- İnternet kullanımının artması ile yönetim ve karmaşıklık artmıştır. Kişilere özel içerik üretimi için matematiksel modellerin kullanılması gerekmektedir.
- Fonksiyon bir çıktı döndürmelidir; prosedür ise değer döndürmüyordur (void).

# Akış Şemaları

![Akis](https://github.com/ramisyk/egitim-notlarim/blob/master/algoritma-programlama-veri-yapilari/1_Algoritma/kaynak/Akis1.png)

# Sözde Kod

Yapılandırılmış bir metin şeklindedir, bir program ya da akış şeması değildir. Algoritmanın okunurluluğunu artıırmak ve algoritma analizini kolaylaştırmak için kullanılır.

**Örnek:** 1'den n'e kadar olan sayıları ekrana yazdıran algoritmanın sözde kodu aşağıdaki gibidir.

*ekranaYaz(n)*
1. *n* değerini oku
2. i <- 0
3. **while** i <= n **do**
4.   *i* ekrana yaz
5. **end while**

# Algoritmanın Morfolojisi

- **Değişken:** Bilgisayar hafızasında değer depolamak ve kullanmak için ayrılan alanı belirten yapılar.
- **Veri türü:** Tarih, sayı, metin gibi verilerin hangi şekilde saklanılması gerektiğini belirtir. Veri türlerinin işlemleri kendine has olduğundan doğru veri tipini seçmek işlemleri kolaylaştırır.
- **Bir kod satırı:** Algoritma içindeki tek bir adım, ifade.

## Algoritma ilkeleri

- İşlem adımları kesindir.
- Her girdi için çıktı değeri gözlemlenir (deterministik).
- Her girdide çıkış değeri üretmek için sonlu sayıda prosedür üretilir (sonluluk).
- Sonuç garantisi vardır.
- Fonksiyonlar, özel bir alana değil istenilen formdaki tüm değerler için kullanılmalıdır (genellilik).

# Algoritma Türleri


## Direkt Algoritmalar

- Belirli koşullarda kendini tekrar eden kod bloklarına **iterasyon** denir. Direkt algortimalarda iterasyon durumu söz konusu değildir.
**Örnek:** İkinci dereceden bir denklemin köklerini bulmak için direkt algoritmalardan faydalanarak delta değerini de denklemin köklerini iterasyona gerek duymaksızın bulabiliriz.

## Ardışık Algoritmalar

- Döngülerin ve recursive yapıların kullanıldığı yapılarda çözüme ulaşmak için algoritma iterasyon gerçekleştirmek durumunda kalır ve bu algoritmalar ardışık algoritma olarak adlandırılır.
**Örnek:** Faktoriyel hesaplamak için sürekli çarpma işlemi gerçekleştirmek. 5! = 5 x 4!, 5! = 5 x (4 x 3!) gibi.

### Yakınsak Algoritmalar

- Çözüme doğru yakınsayan ardışık algoritmalardır. Kesin bir çözüm bulunamaz ancak en yakın sonuç çözüm olarak belirtiler.

### Sonlu Algoritmalar

- İterasyonların bir sonunun olduğu ve çözümün kesin olduğu algoritmalardır.
- Yol yapılı ve ağaç yapılı olarak ikiye ayrılırlar.

**Yol Yapılı Algoritma:** Dallanma olmadan bir önceki iterasyonları takip eder.

**Ağaç Yapılı Algoritma:**  İterasyonlar paralel dalları oluşturan ağaç şeklindedir. Ağaç arama algoritmaları örnek verilebilir.
