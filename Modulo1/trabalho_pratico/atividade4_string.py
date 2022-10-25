# -*- coding: iso-8859-1 -*-
'''
Created on 24 de out. de 2022

@author: daline
'''
# variáveis do tipo string
nome = 'João da Silva'
cidade = 'São Paulo'
cpf = '123.456.789-00'

#exibe variaveis em maiusculo
print(nome.upper())
print(cidade.upper())
#exibe variaveis em minusculo
print('\n',nome.lower())
print(cidade.lower())

#inicializa i para entrada no for
i = 0
#Exibe a posição do caractere ã, se presente na variavel nome
for i in range(len(nome)):
    if nome[i] == 'ã':
        print('\nO caracter "ã" aparece na posicao: ',str(i))
    else:
        continue
    
#inicializa i para entrada no for
i = 0
#Exibe a posição do caractere ã, se presente na variavel cidade
for i in range(len(cidade)):
    if cidade[i] == 'ã':
        print('O caracter "ã" aparece na posicao: ',str(i))
    else:
        continue

#Exiba o número de caracteres de cada variável
print('\nO nome ', nome, 'possui ', len(nome), ' caracteres.')
print('A cidade ', cidade, 'possui ', len(cidade), ' caracteres.')
print('O CPF ', cpf, 'possui ', len(cpf), ' caracteres.')

#remove ponto e hifem do cpf
cpf = cpf.replace('.', '')
cpf = cpf.replace('-', '')
print('\nExibindo o CPF limpo: ', cpf)
