# tentativas = False
# while tentativas == False:
#     try:
#         idade = int(input("Informe a idade: "))
#         if idade >= 16:
#             print("apto a votar")
#             tentativas = True
#         else:
#             print("Não tem idade minima para votar.")
#             tentativas = True
#     except:
#         print("Você não digitou um número, tente novamente.")
#         tentativas = False
#########################################
# op = str(input("Deseja somar? (S/N): ")).upper()

# if (op == "S"):
#     x = int(input("Digite o primeiro numero: "))
#     y = int(input("Digite o segundo numero: "))
#     resultado = x + y
#     print(f"O resultado da soma é: {resultado}")
# print("Até a próxima!")
#########################################

# tentativa = False
# while tentativa == False:
#     try:
#         op = str(input("Deseja somar(S) ou multiplicar(M)?")).upper()
#         x = int(input("Digite o primeiro numero: "))
#         y = int(input("Digite o segundo numero: "))
        
#         if op == "S":
#             r = x + y
#             print(f"O resultado da soma é: {r}")
#             tentativa = True
#         elif op == "M":
#             r = x * y
#             print(f"O resultado da multiplicação é: {r}")
#             tentativa = True
#         else:
#             print(f"Você digitou o valor {op}, o valor esperado é S ou M:")
#             tentativa = False
#     except:
#         print("Você não digitou uma letra ou número, tente novamente!")
#         tentativa = False
#########################################
# valor = False
# while valor == False:
#     try:
#         nota = float(input())
#         if nota >= 7:
#             print("Aprovado")
#         elif nota < 7 and nota >= 1.7:
#             print("Em exame")
#         elif nota < 1.7:
#             print("Reprovado")
#         valor = True

#     except:
#         print("Valor digitado diferente de float, tente novamente: ")
#         valor = False
#########################################
# 01
# valor = False
# while valor == False:
#     try:
#         nota1 = float(input("Digite a primeira nota: "))
#         nota2 = float(input("Digite a segunda nota: "))
#         nota3 = float(input("Digite a terceira nota: "))
#         media = (nota1 + nota2 + nota3)/3
#         print(media)
#         if media >= 6 and nota1>=5 and nota2>=5 and nota3>=5:
#             print("Aprovado")
#         else:
#             print("Reprovado")
#         valor = True

#     except:
#         print("Valor digitado diferente de float, tente novamente: ")
#         valor = False
#########################################
# 02
# num1 = float(input("Digite o primeiro numero: "))
# num2 = float(input("Digite o segundo numero: "))

# if num2 == 0:
#     print("Erro: divisão por zero!")
# else:
#     div_num = num1 / num2
#     print(div_num)
#########################################
# 03
# num1 = int(input("Digite o primeiro numero: "))
# num2 = int(input("Digite o segundo numero: "))

# if num1 > num2:
#     print(num1)
# elif num2 > num1:
#     print(num2)
# else:
#     print(num1, num2)
#########################################
# 04
# num1 = int(input("Digite o primeiro numero: "))

# resultado = num1 % 2
# if resultado == 0:
#     print("Par")
# else:
#     print("Ímpar")
#########################################
# 05
# num1 = int(input("Digite o primeiro numero inteiro: "))
# num2 = int(input("Digite o segundo numero inteiro: "))
# num3 = int(input("Digite o terceiro numero inteiro: "))

# if num1>num2 and num1>num3:
#     print(num1)
# elif num2 > num1 and num2>num3:
#     print(num2)
# else:
#     print(num3)
#########################################
# 06
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))

imc = (peso/altura**2)
print(imc)
if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("Saudável")
elif imc >= 25 and imc < 30:
    print("Peso em excesso")
elif imc >= 30 and imc < 35:
    print("Obesidade Gradu 1")
elif imc >= 35 and imc < 40:
    print("Obesidade Gradu 2 (severa)")
elif imc >= 40:
    print("Obesidade Gradu 3 (mórbida)")