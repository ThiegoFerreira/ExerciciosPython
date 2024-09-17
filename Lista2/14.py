nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

res = (nota1 + nota2)/2

if nota1 >0 and nota1 <=10:
    if nota2 >0 and nota2 <= 10:
        print("A média é", res)
else:
    print("Nota inválida!")
