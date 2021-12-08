import time

notaUm = float(input("Insira a Primeira Nota: "))
notaDois = float(input("Insira a Segunda Nota: "))
notaTres = float(input("Insira a Terceira Nota: "))
notaQuatro = float(input("Insira a Quarta Nota: "))

media = lambda valorUm, valorDois, valorTres, valorQuatro: (valorUm + valorDois + valorTres + valorQuatro)/4
mediaAlunoUm = media(notaUm, notaDois, notaTres, notaQuatro)

print("Seu resultado foi...")
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
if mediaAlunoUm >= 7:
    print(f"Aprovado com {mediaAlunoUm}!!")
else:
    print(f"Reprovado com {mediaAlunoUm} ...")