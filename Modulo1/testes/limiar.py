'''
Created on 23 de out. de 2022

@author: daline
'''
# define o valor do limiar
limiar = 5

menores = [] # cria lista menores
maiores = [] # cria lista maiores

# divide os numeros de 1 a 10 em maiores e menores
for i in range(11):
    if (i < limiar):
        menores.append(i)
    elif (i > limiar):
        maiores.append(i)

# imprime na tela os valores das listas
print('Resultado final')
print('menores:', menores)
print('maiores:', maiores)