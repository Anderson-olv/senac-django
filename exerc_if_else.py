# 01
# data_nascimento = int(input("Digite o ano em que você nasceu: "))

# voto = 2024 - data_nascimento

# if voto >= 18:
#     print("Podera votar este ano.")
# else:
#     print("Não podera votar este ano.")

# 02
# senha = int(input("Digite a senha: "))

# if senha == 1234:
#     print("ACESSO PERMITIDO")
# else:
#     print("ACESSO NEGADO")

# 03
# maca = int(input("Informe a quantidade de maçãs compradas: "))
#
# if maca < 12:
#     total = maca * 0.30
#     print(f"Total da compra: {total}")
# else:
#     total = maca * 0.25
#     print(f"Total da compra: {total}")

# 04
# n1 = int(input("Informe um valor inteiro: "))
# n2 = int(input("Informe um valor inteiro: "))
# n3 = int(input("Informe um valor inteiro: "))
#
# if n1 > n2:
#     n1, n2 = n2, n1
# if n2 > n3:
#     n2, n3 = n3, n2
# if n1 > n2:
#     n1, n2 = n2, n1
#
# print(n1, n2, n3)

# 05
# altura = float(input("Digite sua altura: "))
# sexo = int(input("Digite seu sexo 1=feminino ou 2=masculino): "))
#
# if sexo == 2:
#     peso_ideal = (72.7 * altura) - 58
#     print(f"Seu peso ideal é: {peso_ideal} kg")
# elif sexo == 1:
#     peso_ideal = (62.1 * altura) - 44.7
#     print(f"Seu peso ideal é: {peso_ideal} kg")

# 06 e 07
# lados = int(input("Digite o número de lados de um polígono: "))
# medida = float(input("Digite a medida do lado (em cm): "))
#
# if lados < 3:
#     print("NÃO É UM POLÍGONO.")
# elif lados == 3:
#     area = (medida ** 2 * (3 ** 0.5)) / 4
#     print(f"TRIÂNGULO - valor da área: {area}")
# elif lados == 4:
#     area = medida ** 2
#     print(f"QUADRADO - valor da área: {area}")
# elif lados == 5:
#     print("PENTÁGONO.")
# else:
#     print("POLÍGONO NÃO IDENTIFICADO.")

# 08
# primeiro_lado = float(input("Digite o comprimento do primeiro lado do triângulo: "))
# segundo_lado = float(input("Digite o comprimento do segundo lado do triângulo: "))
# terceiro_lado = float(input("Digite o comprimento do terceiro lado do triângulo: "))
#
# if primeiro_lado == segundo_lado == terceiro_lado:
#     print("Triângulo Equilátero")
# elif primeiro_lado == segundo_lado or primeiro_lado == terceiro_lado or segundo_lado == terceiro_lado:
#     print("Triângulo Isósceles")
# else:
#     print("Triângulo Escaleno")

# 09
# angulo1 = float(input("O valor do primeiro ângulo do triângulo: "))
# angulo2 = float(input("O valor do segundo ângulo do triângulo: "))
# angulo3 = float(input("O valor do terceiro ângulo do triângulo: "))
#
# if angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
#     print("Triângulo Retângulo")
# elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
#     print("Triângulo Obtusângulo")
# else:
#     print("Triângulo Acutângulo")
