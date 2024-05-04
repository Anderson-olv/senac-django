# 01
# numero = int(input("Digite um numero para saber a tabuada do mesmo: "))

# multi = 1
# while (multi <= 10):
#     print(numero * multi)
#     multi += 1

# 02
# pergunta = input("Você deseja somar dois números(sim ou nao)? ")

# while pergunta == "sim":
#     n1 = float(input("Digite o primeiro numero: "))
#     n2 = float(input("Digite o segundo numero: "))
#     print(f"Resultado da soma: {n1+n2}")
#     pergunta = input("Você deseja somar dois números novamente(sim ou nao)? ")

# 03
# numero = int(input("Digite um numero para saber seu fatorial: "))

# laco = numero - 1
# fatorial = numero
# while laco >= 1:
#     fatorial = fatorial * laco
#     laco = laco - 1
# print(fatorial)

# 04
# par = 100
# while par != 0:
#     par = par - 2
#     print(par)

# 05
# n1 = int(input("Digite um numero para saber se o numero é primo ou composto: "))

# n_divisoes = 1
# primo = n1
# contador = 0

# while n_divisoes <= n1:
#     if n1 % n_divisoes == 0:
#         contador += 1
#     n_divisoes += 1

# if n1 == 1:
#     print("Esse numero não é primo e nem composto.")
# elif contador == 2:
#     print("Primo")
# else:
#     print("Composto")


# 06
# regressiva = 10

# while regressiva > 0:
#     print(regressiva)
#     regressiva = regressiva - 1

##############################################################
# 1)
# saldo = 0
# sair = False

# while sair == False:
#     opcao = str(input("Escolha 1 das opções: \n(a) consulta saldo\n(b) saque\n(c) depósito\n(d) sair\n"))

#     if opcao == "a":
#         print(f"O valor do saldo é: {saldo:.2f}")
#     elif opcao == "b":
#         saque = float(input("Informe o valor que deseja sacar: "))
#         saldo = saldo - saque
#     elif opcao == "c":
#         deposito = float(input("Informe o valor que deseja depositar: "))
#         saldo = saldo + deposito
#     elif opcao == "d":
#         sair = True
#     else:
#         print("Comando de entrada invalido, tente novamente.")

# 2)
# n1 = int(input("Informe a altura da estrutura(número de linhas): "))
# multi = 1

# while n1 > 0:
#     print("*"*multi)
#     multi += 1
#     n1 -= 1

# 3)
# nu_alunos = int(input("Informe o numero de alunos: "))
# alunos = nu_alunos
# soma_notas = 0

# while alunos > 0:
#     nota_aluno = float(input(f"Digite a nota do aluno: "))
#     soma_notas += nota_aluno
#     alunos -= 1

# media = soma_notas / nu_alunos

# print(f"A média das notas da turma foi de: {media:.1f}")

# 4)
# laco = True
# while laco:
#     n1 = int(input("Digite o primeiro numero inteiro: "))
#     n2 = int(input("Digite o segundo numero inteiro: "))
#     if n1 > n2:
#         print(f"O numero de maior valor é: {n1}")
#     elif n2 > n1:
#         print(f"O numero de maior valor é: {n2}")
#     else: 
#         print("Números iguais")
#         laco = False

# 5)
# v_inicial = int(input("Digite o valor inicial do contador: "))
# v_final = int(input("Digite o valor final do contador: "))

# while v_inicial >= v_final:
#     print("Valor final menor ou igual ao valor inicial, tente novamente.\n")
#     v_inicial = int(input("Digite o valor inicial do contador: "))
#     v_final = int(input("Digite o valor final do contador: "))

# contador = v_inicial
# while contador <= v_final:
#     print(contador)
#     contador += 1

# 6)
# Lendo o número inteiro do usuário
# numero = int(input("Digite um número inteiro: "))
# soma = 0
# contador = 1

# while contador <= numero:
#     soma += contador
#     contador += 1

# print(soma)
