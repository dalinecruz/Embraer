# -*- coding: iso-8859-1 -*-
'''
Created on 2 de nov. de 2022

@author: daline
'''
# Atividade 5
# Declaração da lista a ser trabalhada no exercicio
lista = [1,2,3,4,5,6,7,8,9]

# Encontra número ímpar
def impar (lista):
    lista_impar = [numero for numero in lista if numero%2 != 0]
    return lista_impar

# Encontra e retorna o maior número impar presente na lista
def maior_impar(lista):
    maior = max(impar(lista))
    return maior

# Encontra e retorna o menor número impar presente na lista
def menor_impar(lista):
    menor = min(impar(lista))
    return menor

# Encontra e retorna o maior e o menor número ímpar presentes na lista
# def menor_impar(lista):

print(f'Maior número da lista: {maior_impar(lista)}')
print(f'Menor número da lista: {menor_impar(lista)}')