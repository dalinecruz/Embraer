# -*- coding: iso-8859-1 -*-
'''
Created on 2 de nov. de 2022

@author: daline
'''
# rela��o dos nomes
nomes = ['Maria', 'Julieta', 'Fernando', 'Cristiano', 'Julieta', 'Maria', 'Fernando', 'Cl�udio']

# estrutura que ir� armazenar o n�mero de letras de cada nome
qtd_letras = {}

# calcula o tamanho de cada nome (em n�mero de letras) e armazena o valor na estrutura
for nome in nomes:
    qtd_letras[nome] = len(nome)
    
print(len(qtd_letras))
print(len(nomes))
print(type(nomes), type(qtd_letras))


print({nome: len(nome) for nome in nomes if nome == len(nome)})
print({nome: len(nome) for nome in nomes})
print({nome: len(nome)} for nome in nomes if nome == len(nome))