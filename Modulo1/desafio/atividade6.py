# -*- coding: iso-8859-1 -*-
'''
Created on 2 de nov. de 2022

@author: daline
'''
# relação de dias da semana que cada médico atende
cardiologista = {'terca', 'quarta'}
ortopedista = {'terca', 'quinta'}
dermatologista = {'segunda', 'quarta', 'sexta'}
neurologista = {'terca', 'quinta', 'sexta'}
psiquiatra = {'segunda', 'quarta', 'sexta'}

# Calcula quais os dias possíveis para dois médicos
def disp_dois_especialistas(medico01, medico02):
    dois_medicos = medico01 & medico02
    return dois_medicos

# Calcula quais os dias possíveis para três médicos
def disp_tres_especialistas(medico01, medico02, medico03):
    tres_medicos = medico01 & medico02 & medico03
    return tres_medicos

# Executa as funções e imprime seus resultados
print(f'Os dias disponiveis são: {disp_dois_especialistas(neurologista,ortopedista)}.')
print(f'Os dias disponiveis são: {disp_tres_especialistas(dermatologista, neurologista ,psiquiatra)}.')