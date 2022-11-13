# -*- coding: iso-8859-1 -*-
'''
Created on 7 de nov. de 2022

@author: daline
'''
# importação das bibliotecas
import numpy as np
import pandas as pd

## Código 8 ##
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5 , 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1,3,2,3,2,3,1,1,2,1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b,', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

## Código 9 ##
df = pd.DataFrame(data=data, index=labels)
print(df)
print(df.shape)
print(df['animal'].value_counts())
print(df.describe())
print(df.iloc[:, 3])
print(df['visits'])
print(df.iloc[:, -2])
print(df.loc[:, 'visits'])
print(df.sort_values(by='visits', ascending=False))
print(df.sort_values(by='visits'))

## Código 10 ##
y_true = np.array([1.,2.,1.])
y_pred = np.array([1.1,1.98,1.05])
print(np.sqrt(((y_true-y_pred)**2).mean()))