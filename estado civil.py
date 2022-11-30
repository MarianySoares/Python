nome = 'm'
while (len(nome) <= 3):
    nome = str (input ('informe um nome'))
    
idade = 15
while (idade > 150 and idade < 0 ):
    idade = int ( input ( 'informe a idade'))

salario = 2
while (salario < 0):
    salario = float( input('informe um salario'))

sexo = 'f'
while sexo != 'f' ^ sexo != 'm':
    sexo = str (input(' insira a inicial do seu sexo'))

estadoCivil = 'n'
while (estadoCivil != 's' ^ estadoCivil != 'c' ^ estadoCivil != 'v' ^ estadoCivil != 'd'):
    estadoCivil = str (input('informe a incial do seu estado civil'))