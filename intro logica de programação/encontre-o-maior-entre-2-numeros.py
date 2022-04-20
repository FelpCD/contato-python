# condicionais 
#if, elif, else

# Encontre o mair entre 2 números 
'''
Piseudocodigo

input primeiro_valor
input segundo_valor
if primeiro_valor > segundo_valor 
   print o primeiro valor é maior
else
   printe o segundo valor é mair 

'''

primeiro_valor = input('Digite aqui o 1º valor:')
segundo_valor = input('Digite aqui o 2º valor:')
if int(primeiro_valor) > int(segundo_valor): # (int) transforma a resposta de string em valor inteiro
    print('O primeiro valor é mair!')
else:  # Caso contrario 
    print('O segundo valor é maior!')