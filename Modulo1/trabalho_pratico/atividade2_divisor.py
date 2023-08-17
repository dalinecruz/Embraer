# -*- coding: iso-8859-1 -*-
'''
Created on 24 de out. de 2022

@author: daline
'''
# declaração das variáveis
divisor = 1
inicio = 0
fim = 1000

#solicita entrada do usu?rio e atribui valor a variavel divisor
divisor = int(input('Insira um número e informarei seus múltiplos no intervalo de 0 a 1000: '))

# verifica quais números são divisíveis pelo conteudo da variavel divisor, e exibe aqueles que são
for numero in range(inicio, fim):
    if numero % divisor == 0:
        print(numero)