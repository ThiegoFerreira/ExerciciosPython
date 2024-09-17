num1 = float(input("Informe um número: "))
num2 = float(input("Informe um segundo número: "))
if num1 > num2:
    print("O", num1, "é maior que ",num2)
elif num2 > num1:
    print("O", num2, "é maior que ",num1)
elif num1 == num2:
    print("Números iguais!")