# Temel Veri Yapıları

## Veri Yapılarına Giriş

Veri yapısı, veri üzerinde erişim, depolama ve organizasyon gibi kavramları temsil eder ve verinin değeri, veriler arasındaki ikişkileri veri üzerinde uygulanabilecek işlemleri kapsar.

## Verinin Alt ve Üst Limitleri

int sayi = 15; => bellekte sayi isminde yer oluşturur.
&sayi => sayi değişkenin bellekteki adresi.
SByte & Byte -> 1 byte (işaretli / işaretsiz)
int16 -> 2 byte
int32 -> 4 byte
int64 -> 8 byte

|**SByte için**         |**Byte için**          |
|-----------------------|-----------------------|
|1000 0000 = -128 (Min) |0000 0000 = 0 (Min)    |
|1000 1111 = -15        |0000 1111 = 15         |
|1000 0001 = -1         |0000 0001 = 1          |
|                       |                       |
|0000 0000 = 0          |0000 0000 = 0          |
|                       |                       |
|0000 0001 = 1          |1000 0001 = 129        |
|0000 1111 = 15         |1000 1111 = 143        |
|0111 1111 = 127 (Max)  |1111 1111 = 255 (Max)  |