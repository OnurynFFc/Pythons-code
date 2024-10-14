# Desenvolva um jogo de adivinhação em Python, onde o programa escolhe um número aleatório e o usuário deve tentar adivinhar qual é esse número.
# O programa deve fornecer dicas ao usuário, informando se o número escolhido é maior ou menor do que o número que ele está tentando adivinhar.
# O jogo deve continuar até que o usuário acerte o número ou decida sair do jogo.
 
import random

N_aleatorio= random.randint(59, 70)

#numero do usuario

n_user= int(input("diga um valor de 1 a 60:"))

# while n_user != N_aleatorio:
#     print("digite o valor errado",N_aleatorio)
#     continue

if n_user==N_aleatorio:
    print("Você acertou o valor:")
else:
     print("Você errou o valor:")
     print("valor certo:",random.randint(1, 60))
    # print("Valor correto:",N_aleatorio)