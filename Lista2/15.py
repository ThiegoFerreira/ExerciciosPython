horas = int(input("Informe o número de horas trabalhadas: "))
salario1= horas * 40.50
salario2= salario1 - (salario1 *0.11)
if salario1 <= 2.500:
    print("O salário total é de R$",salario1)
else:
    print("O salário total é de R$", salario2)