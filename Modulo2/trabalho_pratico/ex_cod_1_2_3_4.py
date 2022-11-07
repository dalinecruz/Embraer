# -*- coding: iso-8859-1 -*-
'''
Created on 7 de nov. de 2022

@author: daline
'''
# importação das bibliotecas
import numpy as np

## Código 1 ##
Z = np.zeros((4, ))
print("Z: ", Z)

## Código 2 ##
Z = np.zeros((4, ))
Z[1] = 1.
print("Z: ", Z)

## Código 3 ##
Z = np.zeros((4, ))
Z[1:] = 1.
print("Z: ", Z)

## Código 4 ##
Z = np.zeros((4, ))
Z[:3] = 1.
print("Z: ", Z)