# -*- coding: iso-8859-1 -*-
'''
Created on 24 de out. de 2022

@author: daline
'''
# declara��o das vari�veis
inicio = 0
fim = 100
# verifica quais n�meros s�o divis�veis por cinco, e exibe aqueles que s�o
for numero in range(inicio, fim):
    if numero % 5 ==  0:
        print(numero)
