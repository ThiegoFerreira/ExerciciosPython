print("*"*100,"\nCalculadora 2024\n\nAdição(opção 1)\nSubtração(opção 2)\n\
Multiplicação(opção 3)\nDivisão(opção 4)\nSaída(opção 5)")
opcao=1
while opcao > 0 and opcao <5:
    opcao=int(input("\n\nDigite a opção desejada: "))
    num1= int(input("Digite o primeiro número: "))
    num2=int(input("Digite o segundo número: "))
    if opcao == 1:
        soma=num1 + num2
        print(f"{num1} + {num2} = {soma}")
    elif opcao == 2:
        if num1<num2:
            sub = num2-num1
        elif num1> num2:
            sub = num1-num2
        print(f"{num1} - {num2} = {sub}")
    elif opcao ==3:
        mult = num1*num2
        print(f"{num1} * {num2} = {mult}")
    elif opcao ==4:
        div = num1/num2
        print(f"{num1} / {num2} = {div}")
    elif opcao <1 and opcao >5:
        opcao=int(input("\n\nDigite a opção desejada: "))
        num1= int(input("Digite o primeiro número: "))
        num2=int(input("Digite o segundo número: "))
if opcao==5:
    print("Fim!")
