valUm = 10
valDois = 5

soma = lambda valorUm, valorDois: valorUm + valorDois
subtracao = lambda valorUm, valorDois: valorUm - valorDois
multiplicacao = lambda valorUm, valorDois: valorUm * valorDois
divisao = lambda valorUm, valorDois: valorUm / valorDois
resto = lambda valorUm, valorDois: valorUm % valorDois

print(f"Soma dos valores: {soma(valUm,valDois)}")
print(f"Subtracao dos valores: {subtracao(valUm,valDois)}")
print(f"Multiplicacao dos valores: {multiplicacao(valUm,valDois)}")
print(f"Divisao dos valores: {divisao(valUm,valDois)}")
print(f"Resto dos valores: {resto(valUm,valDois)}")