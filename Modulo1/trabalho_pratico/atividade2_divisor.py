# -*- coding: iso-8859-1 -*-
'''
Created on 24 de out. de 2022

@author: daline
'''
# declara��o das vari�veis
divisor = 1
inicio = 0
fim = 1000

#solicita entrada do usu?rio e atribui valor a variavel divisor
divisor = int(input('Insira um n�mero e informarei seus m�ltiplos no intervalo de 0 a 1000: '))

# verifica quais n�meros s�o divis�veis pelo conteudo da variavel divisor, e exibe aqueles que s�o
for numero in range(inicio, fim):
    if numero % divisor == 0:
        print(numero)