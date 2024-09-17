num1 = float(input("Digite o primeiro número: "))
operacao = input("Informe a operação desejada: ")
num2 = float(input("Informe o segundo número: "))

if operacao == "+":
    res = num1 + num2
    print(f"A soma de {num1} com {num2} é igual {res}")
elif operacao == "-":
    res = num1 - num2
    print(f"A subtração de {num1} com {num2} é igual {res}")
elif operacao == "*":
    res = num1 * num2
    print(f"A multiplicação de {num1} com {num2} é igual {res}")
elif operacao == "/":
    res = num1 - num2
    print(f"A divisão de {num1} com {num2} é igual {res}")
else:
    print("Operação inválida!")
