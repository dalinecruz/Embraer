# -*- coding: iso-8859-1 -*-
'''
Created on 24 de out. de 2022

@author: daline
'''
# declara��o das vari�veis
inicio = 100
fim = 501

# verifica quais n�meros s�o divis�veis por dois, cinco ou 7, e exibe aqueles que s�o
for numero in range(inicio, fim):
    if numero % 2 == 0 or numero % 5 == 0 or numero % 7 == 0:
        print(numero)