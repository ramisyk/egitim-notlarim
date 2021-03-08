#kütüphane ekleme
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#veri yükleme
veriler = pd.read_csv('veriler.csv')
#print(veriler)

boy = veriler[['boy']]
#print(boy)

boykilo = veriler[['boy', 'kilo']]
print(boykilo)