# -*- coding: iso-8859-1 -*-
'''
Created on 24 de out. de 2022

@author: daline
'''
# declaração das variáveis
inicio = 100
fim = 501

# verifica quais números são divisíveis por dois, cinco ou 7, e exibe aqueles que são
for numero in range(inicio, fim):
    if numero % 2 == 0 or numero % 5 == 0 or numero % 7 == 0:
        print(numero)