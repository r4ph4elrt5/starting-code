import random as rd

numero_escondido = rd.randint(0, 100)

print('\nVou escolher um numero de 0 a 100, vou deixar você chutar até acertar e ainda vou falar se esta maior ou menor que o numero sortiado!')
chute = None

while  numero_escondido != chute:
    
    chute = int(input('Qual seria seu chute: '))
    
    if numero_escondido > chute:
        print('<<<<<<<<<<<<<<<<<<<<< Seu chute é menor que o Numero Sortiado!\n')

    elif numero_escondido == chute:
        print(' Você Acertou, Parabens!!!!\n')

    else:
        print('Seu chute é maior que o Numero Sortiado!>>>>>>>>>>>>>>>>>>>>>\n')

