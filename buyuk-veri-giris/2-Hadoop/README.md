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