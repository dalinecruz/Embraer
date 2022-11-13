# -*- coding: iso-8859-1 -*-
'''
Created on 7 de nov. de 2022

@author: daline
'''
# importação das bibliotecas
import numpy as np

## Código 5 ##
A = np.ones((2,2))
X = 2*A
print("X:\n", X)

X = np.ones((2, 2)) + np.ones((2, 2))
print("X:\n", X)


X = 2 * np.ones((2, 2))
print("X:\n", X)

X = np.array([2.] * 4).reshape(2, 2)
print("X:\n", X)
