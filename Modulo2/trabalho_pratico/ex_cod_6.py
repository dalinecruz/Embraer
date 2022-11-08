# -*- coding: iso-8859-1 -*-
'''
Created on 7 de nov. de 2022

@author: daline
'''
# importação das bibliotecas
import numpy as np

## Código 6 ##
X = np.array([[1,2],[3,4]])
Y = X[0,:]
Y[1] = 10
print("X:\n", X)