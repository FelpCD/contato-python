#Condicionais 
#if, elif, else

#if = Se/comparação 
#else = Caso contrario

'''
SITUAÇÃO 
Eu chequei atrasado na aula, ainda posso entrar?
CONDIÇÃO 
Se essa não for a terceira vez chegando atrasado, então pode entrar
CONSEQUÊNCIA
Caso contrario será suspenso. 
'''

numero_atrasos = 3
if numero_atrasos >=3:
    print('Você esta suspenso!')
elif numero_atrasos == 1: # (elif) Quando temos varia avaliações a serem feitas
    print('Você esta liberado, caso você falte tome mais 2 faltas irá ser suspenso.')
elif numero_atrasos == 2:
    print('Você esta liberado, caso você falte tome mais 1 faltas irá ser suspenso.')
else:
    print('Você esta liberado!')