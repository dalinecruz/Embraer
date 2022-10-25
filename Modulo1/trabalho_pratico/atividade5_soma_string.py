# -*- coding: iso-8859-1 -*-
'''
Created on 24 de out. de 2022

@author: daline
'''
#inicializa as variaveis
numero = '127957'
soma = 0

#converte caracteres para inteiro e soma
for i in range(len(numero)):
    soma = soma + int(numero[i])
print(soma)
