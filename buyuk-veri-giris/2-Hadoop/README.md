# 2 - Hadoop ve Bileşenleri

Hadoop, büyük veri kümeleri ile birden fazla makinede paralel olarak işlem yapmamızı sağlayan java ile geliştirilen açık kaynak kodlu kütüphanedir.

<!--Hadoop Bileşen Tablosu-->
![hadoopBilesenTablosu](https://github.com/ramisyk/egitim-notlarim/blob/master/buyuk-veri-giris/2-Hadoop/kaynak/1-hadoopBilesenTablosu.png "Hadoop Bileşen Tablosu")

Hadoop temel olarak HDFS, YARN ve MapReduce modüllerini kullanmakta ve bu modüller arası iletişimi Hadoop Common ile yapmaktadır.

Hadoop içerisinde büyük verileri sakladığımız bileşene HDFS denir. HDFS verileri parçalara ayırarak kopyalı şekillerde saklar ve cluster üzerinde verileri tutar. Birden fazla makinenin arasında iletişim olduğunda cluster yapı oluşur.
input file -> parçalara ayrılır (default 128 Mb lik parçalar) -> parçalanan verileri parça sayısı kadar node a dağıtır

<!--HDFS Veri Saklama Sistemi-->
![hdfsCluster](https://github.com/ramisyk/egitim-notlarim/blob/master/buyuk-veri-giris/2-Hadoop/kaynak/2-hdfsCluster.png "HDFS Veri Saklama Sistemi")
Replication factor her parçanın kaç makinede saklanması gerektiğini belirtmektedir. Bu durumda herhagi bir makinede sorun olduğunda veri kaybı yaşamamız önlenecektir.

Makinelerin herhangi biri kapandığında ya da makine makine eklendiğinde ana makine verileri replication factor a uygun olarak yeniden dağıtır.

Hadoop içinde verileri paralel olarak işleyebileceğimiz bileşen MapRaduce'tur.
Apache Pig, Apache Hive gibi yöntemler vardır. (pig kullanımı kalmamıştır, spark mapReduce a rakip şekilde kullanılmaktadır.)

Adımlar sırasıyla:
Input -> Splitting -> Mapping -> Shuffling -> Reducing -> Final Result


**Splitting :** Tamamında işlem yapmak yerine daha kolay işlem yapabilmek için parçalara ayırır (böl ve yönet)
**Mapping :** Bölünen datada istenilen analiz yapılır.
**Shuffling :** Veriler node lar üzerinde işlem yapar. Bölünen datalar üzerinde mapping e uygun işlem yapılır.
**Reducing :** Yapılan işlemi toplar.
**Final Result :** Reduce sonucunu toplar.

Variler üzerinde kaynak yönetimi, uygulama kullanımı ve ayarlamalar yapmaya olanak sunan bileşen YARN dır.
![yarn](https://github.com/ramisyk/egitim-notlarim/blob/master/buyuk-veri-giris/2-Hadoop/kaynak/3-yarn.png "YARN")

## HDFS Komutları
Dataseti HDFS üzerinde yönetmek için kullanılan komutlardır. Linux işletim sistemi komutları ile aynıdır.
Tüm komutlar "hdfs dfs" ile başlar.

- hdfs dfs -mkdir /(location) : belirtilen konuma klasör oluşturma.
- hdfs dfs -copyFromLocal /(sourceLocation) /(targetLocation) : Bilgisayardaki kaynaktan hdfs e dosya kopyalar.