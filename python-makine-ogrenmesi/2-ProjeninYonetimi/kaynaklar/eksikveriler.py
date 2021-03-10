#kütüphane ekleme
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#veri yükleme
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