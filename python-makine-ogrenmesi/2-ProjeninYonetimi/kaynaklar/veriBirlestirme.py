#1-kütüphane ekleme
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#2-Veri Önişleme
#2.1-veri yükleme
veriler = pd.read_csv('eksikveriler.csv')
#print(veriler)

boy = veriler[['boy']]
#print(boy)

boykilo = veriler[['boy', 'kilo']]
print(boykilo)


#eksik veriler
from sklearn.impute import SimpleImputer 

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
#nan değerleri ortalama değer ile değiştir.
Yas = veriler.iloc[:,1:4].values
#iloc : integer location 
#[:,1,4] => iki nokta bütün satırları getiriyor, 1. sütundan 4. sütuna kadar

print(Yas)

imputer = imputer.fit(Yas[:,1:4]) #=>öğrenme işlemini sağlıyor
Yas[:,1:4] = imputer.transform(Yas[:,1:4]) #değerlerin değiştirilmesi işlemi

# Kategorik verilerin dönüşümü - encoder : Kategorik verilerden Numerik verilere dönüş sağlar
ulke = veriler.iloc[:,0:1].values
print(ulke)

from sklearn import preprocessing

le = preprocessing.LabelEncoder()

ulke[:,0] = le.fit_transform(veriler.iloc[:,0])
print(ulke)

ohe = preprocessing.OneHotEncoder()
ulke = ohe.fit_transform(ulke).toarray()
print(ulke)

#Numpy dizilerinin dataframe e dönüşümü
sonuc = pd.DataFrame(data = ulke, index = range(22), columns=(['fr', 'tr', 'us']))
print(sonuc)

sonuc2 = pd.DataFrame(data = Yas, index = range(22), columns=(['boy', 'kilo', 'yas']))
print(sonuc2)

cinsiyet = veriler.iloc[:,-1]
print(cinsiyet)

sonuc3 = pd.DataFrame(data = cinsiyet, index = range(22), columns=(['cinsiyet']))
print(sonuc3)

#dataframe birleştirme
s = pd.concat([sonuc, sonuc2], axis=1)
print(s)

s2 = pd.concat([s, sonuc3], axis=1)
print(s2)

#verilerin test ve eğitim için bölünmesi
#belirli bir satıra kadar train sonrası test olması için
from sklearn.model_selection import train_test_split

#x ve y bağımlı bağımsız değişken olarak bölmek
"""Ülke, boy, kilo ve yaş a bakarak cinsiyet tahmini yapılacağı durumda
Ülke, boy, kilo ve yaş bilgileri bağımsız değişken olarak bir framede x e gider
cinsiyet farklı bir framede bağımlı değişkin olarak gönderilir."""
x_train, x_test, y_train, y_test = train_test_split(s, sonuc3, test_size=0.33, random_state=0)

#verilerin ölçeklendirilmesi
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)
