# -*- coding: iso-8859-1 -*-
'''
Created on 2 de nov. de 2022

@author: daline
'''
# declara��o de variaveis
pi = 3.141592

# cria��o da fun��o para receber a declara��o de pi
def area1 (r, pi):
    area = pi*(r**2)
    return area
# cria��o da fun��o com valor default para pi
def area2 (r, pi = 3.14):
    area = pi*(r**2)
    return area

print(area1(8, pi))
print(area2(8))