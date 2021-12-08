numeroUm = int(input("Insira o Primeiro Número: "))
numeroDois = int(input("Insira o Segundo Número: "))
numeroTres = int(input("Insira o Terceiro Número: "))

# Váriavel de uma Função
multiplicacao = lambda n1, n2, n3: (n1 * n2 * n3)

print(f"Multiplicacao dos valores: {multiplicacao(numeroUm,numeroDois,numeroTres)}")