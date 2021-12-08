listaValores =  [3,5,6]

opcao = input("Deseja fazer as contas com o próprio número?\n")

soma = lambda valorUm, valorDois: valorUm + valorDois
subtracao = lambda valorUm, valorDois: valorUm - valorDois
multiplicacao = lambda valorUm, valorDois: valorUm * valorDois
divisao = lambda valorUm, valorDois: valorUm / valorDois
resto = lambda valorUm, valorDois: valorUm % valorDois

for n1 in listaValores:
    for n2 in listaValores:
        if (n1 != n2) or (opcao == "Sim" or opcao == "sim"):
            print("---------------------------------------")
            print(f"\n- Calculos de {n1} com {n2}:\n")
            print(f"Soma dos valores: {soma(n1,n2)}")
            print(f"Subtracao dos valores: {subtracao(n1,n2)}")
            print(f"Multiplicacao dos valores: {multiplicacao(n1,n2)}")
            print(f"Divisao dos valores: {divisao(n1,n2)}")
            print(f"Resto dos valores: {resto(n1,n2)}\n\n")
            print("---------------------------------------")

