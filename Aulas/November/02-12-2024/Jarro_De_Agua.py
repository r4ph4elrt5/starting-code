print('\nVocê tem 2 Jarros com Água, sendo um com 5ml de capacidade, outro com 3ml de capacidade, como obter 2ml do liquido ?\n')
print('Opção:')
print(' 1 - Jogar o liquido fora!')
print(' 2 - Beber o liquido todo de um só vez!')
print(' 3 - Enxer o jarro de 5ml e depois de enchelo, usalo para encher o jarro de 3ml, restando assim no jarro de 5ml o valor desejado de 2ml!!!')
print(' 4 - Usar o jarro menor como base e depois colocar tudo dentro um do outro, e depois de beber tudo poderia facilmento ligar para uma outro amigo e pedir ajuda!!!')
print(' 5 - Simplismente quebre os dois jarros!!! \n \n')

timeout = 3
opcao = 0

while opcao != timeout:
    opcao = int(input('Digite de 1 a 5 para selecionar !!!\nQual das opções acima seria a correta: '))

    if opcao == 3:
        print('\nVocê acertou, Parabens !!!\n')

    elif opcao in [1, 2, 4, 5]:
        print('\nErrou, que pena!\n')

    else:
        print('\nDigite uma opção Valida! De 1 a 5 \n')
    







