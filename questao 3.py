print('digite seu nome de usuario')
usuario = input()
print('digite sua senha')
senha = input()
if(usuario == senha):
    print('digite uma senha diferente do nome de uduario')
elif (usuario != senha):
    print('usuario cadastrado com sucesso')