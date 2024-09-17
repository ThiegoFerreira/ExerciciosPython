num1 = int(input("Informe um número inteiro: "))
num2 = int(input("informe um segundo número inteiro: "))

res1 = num1 - num2
res2 = num2 - num1

if num1>num2:
    print("O número maior é ",num1," e a diferença entre ambos é de", res1)
else:
    print("O número maior é ",num2, " e a diferença entre ambos é de", res2)

