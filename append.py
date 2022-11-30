nomes = ['julia', 'mariany', 'nanda', 'amanda', 'emanuele']

nomes.append('camila')
print(nomes[5])

nomes.insert(2,'gabriel')
print(nomes[2])

del nomes[0]
print(nomes[0])

nomes.remove('amanda')

nomes.pop()
print(nomes[3])

nomes.sort()
print(nomes)

print(nomes.count('nanda'))