# -*- coding: iso-8859-1 -*-
'''
Created on 2 de nov. de 2022

@author: daline
'''
# declaração de variaveis
pi = 3.141592

# criação da função para receber a declaração de pi
def area1 (r, pi):
    area = pi*(r**2)
    return area
# criação da função com valor default para pi
def area2 (r, pi = 3.14):
    area = pi*(r**2)
    return area

print(area1(8, pi))
print(area2(8))