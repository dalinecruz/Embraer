'''
Created on 23 de out. de 2022

@author: daline
'''
limiar = 5

menores = [] 
maiores = [] 

for i in range(10):
        if(i<limiar):
                menores.append(i)
        elif(i>limiar):
                maiores.append(i)

print('menores', menores)