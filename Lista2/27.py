print("1-Soma de dois números\n2-Diferença de dois números.\n\
3-Produto entre dois números.\n4-Divisão entre dois números\n")
op = int(input("Informe o número da operação que deseja efetuar: "))
num1 = float(input("Informe o primeiro número real: "))
num2 = float(input("Informe o segundo número real: "))
if op == 1:
    res = num1+num2
    print(f"O resultado da some é {res}")
elif op ==2:
    maior = max(num1,num2)
    menor = min(num1,num2)
    res = maior - menor
    print(f"A diferença entre os números é de {res}")
elif op == 3:
    res = num1*num2
    print(f"O resultado do produto dos números é {res}")
elif op == 4:
    if num2> 0:
        res = num1/num2
        print(f"O resultado da divisão é {res}")
    elif num1 > 0:
        res = num1/num2
        print(f"O resultado da divisão é {res}")
    elif num1 == 0 or num2==0:
        print("O denominador não pode ser zero")
else:
    print("Opção inválida")