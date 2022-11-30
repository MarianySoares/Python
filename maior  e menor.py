condicao = True
soma = 0
numero = []
while condicao:
    num = int(input('digite um numero ou 0 para calcular: '))
    if num != 0:
        soma += num 
        numero .append (num)
    else:
        break
    print('soma: ' + soma )
    print('menor valor:  ' , min(numero))
    print('maior valor:  ' , max(numero))