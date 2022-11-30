numero = 0
while numero != 10:
    numero = int(input('digite um numero'))
    if (numero > 10):
        print('insira um numero meror')
    elif(numero <10):
        print('insira um numero maior')
    else:
        print('voce acertou!')