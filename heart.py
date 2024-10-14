# nm='Universidade Paulista - UNIP'
# n = len(nm)
# print(nm[-4:-2])
nome = input('digite seu nome ')
t_m = len(nome)

if ' ' in nome:
    print(nome, sep='_')
else:
    print(nome)