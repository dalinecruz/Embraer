# -*- coding: iso-8859-1 -*-
'''
Created on 7 de nov. de 2022

@author: daline
'''
# importa��o das bibliotecas
import numpy as np

## C�digo 1 ##
Z = np.zeros((4, ))
print("Z: ", Z)

## C�digo 2 ##
Z = np.zeros((4, ))
Z[1] = 1.
print("Z: ", Z)

## C�digo 3 ##
Z = np.zeros((4, ))
Z[1:] = 1.
print("Z: ", Z)

## C�digo 4 ##
Z = np.zeros((4, ))
Z[:3] = 1.
print("Z: ", Z)