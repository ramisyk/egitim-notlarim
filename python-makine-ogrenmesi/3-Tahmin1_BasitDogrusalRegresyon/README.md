# Tahmin - Basit Doğrusal Regresyon

## Tahmin Nedir?
Sayısal veriler için yapılan tahminler (yaş, gelir düzeyi, maaş, gelecek dönem satışları, döviz kuru) **tahmin** olarak isimlendirilir.

Kategorik verilere bakılarak tahmin yapıldığında ise (cinsiyet, eğitim seviyesi) **sınıflandırma problemi** olarak adlandırılır.

Prediction (tahmin), geçmiş verilere bakarak geçmiş arasında tahmin yapmak ya da eksik verilerin tahmini yapmak için kullanılır.

Forecasting (öngörü), geçmişe bakarak gelecek dönem ile ilgili tahminler, çıkarımlar yapmaktır.

Problem, verilerin dağılımda olduğu noktalardan geçen doğruyu bulmaktır.

Amaç noktaların doğruya uzaklığından hata payını minimuma indirmek...

## Basit Doğrusal Regresyon Model İnşası
fit oluşan modeli inşa etmeye çalışır.

X_train, Y_train üzerinden bilgiler alınarak model inşa edilir ve yapılan modele uygun olarak test verilerinin tahmini karşılaştırılır.

## Uygulanması
X_trainden Y_traini öğreniyor ve sonrasında X_test ten Y_testin tahmin edilmesi bekleniyor.

## Görselleştirilmesi
plot kullanılacak ve eksenler gönderilecek