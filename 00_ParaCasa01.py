#!/usr/bin/env python
# coding: utf-8

# ### 1 - Faça um algoritmo que faça a soma de 4 números e apresente o resultado

# In[1]:


numeroUm = int(input("Insira o Primeiro Número: "))
numeroDois = int(input("Insira o Segundo Número: "))
numeroTres = int(input("Insira o Terceiro Número: "))
numeroQuatro = int(input("Insira o Quarta Número: "))

# Váriavel de uma Função
soma = lambda n1, n2, n3, n4: (n1 + n2 + n3 + n4)

print(f"Soma dos valores: {soma(numeroUm,numeroDois,numeroTres,numeroQuatro)}")


# ### 2 - Faça um algoritmo que recebe 3 valores e faça a multiplicação deles e apresente o resultado

# In[3]:


numeroUm = int(input("Insira o Primeiro Número: "))
numeroDois = int(input("Insira o Segundo Número: "))
numeroTres = int(input("Insira o Terceiro Número: "))

# Váriavel de uma Função
multiplicacao = lambda n1, n2, n3: (n1 * n2 * n3)

print(f"Multiplicacao dos valores: {multiplicacao(numeroUm,numeroDois,numeroTres)}")


# ### 3 - Dados os valores, a = 3, b = 5, c = 6, faça a soma, subtração, divisão e multiplicação entre eles. 

# In[23]:


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


# ### 4 - Imagine que o sistema da empresa aonde trabalha armazene as seguintes informações: nome, idade, data de nascimento, sexo, telefone residencial, telefone celular, email, endereço, cep, estado, cidade e bairro, classifique as variáveis entre seus respectivos tipos!

# In[ ]:


nome = "Pedro" #String
idade = 26 #Int
dataDeNascimento = "01/02/1995" #String
sexo = "Masculino" #String
telefoneResidencial = "(11) 0000-0000" #String -> Como não há processamento envolvendo, seria melhor ser str
telefoneCelular = "(11) 90000-0000" #String -> Como não há processamento envolvendo, seria melhor ser str
email = "emailficticio@gmail.com" #String
endereço = "Rua Fictícia, número 01, Centro, São Paulo - SP" #String
cep = "00000-000" #String -> Como não há processamento envolvendo, seria melhor ser str
estado = "São Paulo" #String
cidade = "São Paulo" #String
bairro = "Centro" #String


# ### 5 - Pensando nas boas práticas já conversadas nas aulas, o que nunca devemos fazer ao declarar uma variável? 

# In[ ]:


Acentuação


# ### 6 - No Python, como identificamos um bloco de comandos? Pelo uso da virgula? Uso de chaves? Ou Identação de código?

# In[ ]:


Identação de Código

