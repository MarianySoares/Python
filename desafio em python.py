from random import *
jonkerPo = ['pedra', 'papel', 'tesoura']
while True: 
    computador = jonkerPo[randint(0,2)]
    jogador = str(input('escolha entre pedra, papel, tesoura ou terminar o jogo'))
    if jogador == 'terminar o jogo':
        break
    elif computador == jogador:
            print('empate') 


    elif jogador == 'pedra':
        if computador == 'papel':
            print('voce perdeu')
        elif computador == 'tesoura':
            print('voce ganhou')


    elif jogador == 'papel':
            if computador == 'tesoura':
                print('voce perdeu')
            elif computador == 'pedra':
                print('voce ganhou')

    elif jogador == 'tesoura':
            if computador == 'pedra':
                print('voce perdeu')
            elif computador == 'papel':
                print('voce ganhou')
    else:
        print('opicao invalida')