# -*- coding: iso-8859-1 -*-
'''
Created on 2 de nov. de 2022

@author: daline
'''
# Atividade 5
# Declara��o da lista a ser trabalhada no exercicio
lista = [1,2,3,4,5,6,7,8,9]

# Encontra n�mero �mpar da lista
def impar (lista):
    lista_impar = [numero for numero in lista if numero%2 != 0]
    return lista_impar

# Encontra e retorna o maior n�mero impar presente na lista
def maior_impar(lista):
    maior = max(impar(lista))
    return maior

# Encontra e retorna o menor n�mero impar presente na lista
def menor_impar(lista):
    menor = min(impar(lista))
    return menor

# Executa as fun��es e imprime os resultados
print(f'Maior n�mero �mpar da lista: {maior_impar(lista)}')
print(f'Menor n�mero �mpar da lista: {menor_impar(lista)}')