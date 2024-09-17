nota1 = float(input("Informe a nota 1: "))
nota2 = float(input("Informe a nota 2: "))
nota3 = float(input("Informe a nota 3: "))

media = (nota1+nota2+(nota3*2))/4

if media >= 6:
    print("A média é",media,". Aprovado!")
else:
    print("Reprovado!")