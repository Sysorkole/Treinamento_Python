import random

def RollDice(dado):
    return random.randrange(dado)+1


### Código de Roll de Dados
dado = int(input("Digite o dado que você deseja rolar: "))
for numero in range(1):
    print(RollDice(dado))
