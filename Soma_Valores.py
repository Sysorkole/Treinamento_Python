numeroUm = int(input("Insira o Primeiro Número: "))
numeroDois = int(input("Insira o Segundo Número: "))
numeroTres = int(input("Insira o Terceiro Número: "))
numeroQuatro = int(input("Insira o Quarta Número: "))

# Váriavel de uma Função
soma = lambda n1, n2, n3, n4: (n1 + n2 + n3 + n4)

print(f"Soma dos valores: {soma(numeroUm,numeroDois,numeroTres,numeroQuatro)}")