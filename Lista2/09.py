num1 = float(input("Informe um número: "))
num2 = float(input("Informe um segundo número: "))
res1 = num1 - num1 - num1
res2 = num1 - num1 - num1
res3 = num2 - num2 - num2
res4 = num2 - num2 - num2

if num1 > 0:
    print("O valor invertido de ", num1," é ",res1)
else:
    print("O valor invertido de ",num1," é ", res2)

if num2 > 0:
    print("O valor invertido de ", num2," é ", res3)
else:
    print("O valor invertido de ", num2, " é ", res4)
