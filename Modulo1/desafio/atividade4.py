# -*- coding: iso-8859-1 -*-
'''
Created on 2 de nov. de 2022

@author: daline
'''
# declara��o da variavel pi
pi = 3.141592

# reescrevendo o codigo da atividade3 utilizando fun��o an�nima
area1 = lambda r,pi: pi*(r**2)
area2 = lambda r,pi=3.14: pi*(r**2)

# executando e imprimindo o resultado das fun��es
print(area1(8, pi))
print(area2(8))