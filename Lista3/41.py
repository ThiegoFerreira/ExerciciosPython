# Crie um programa que calcula a associação em paralelo de dois resistores R1 e R2 fornecidos 
# pelo usuário via teclado. O programa fica pedindo estes valores e calculando até que o usuário
# entre com um valor para resistência igual a zero.

R1=int(input("Informe o valor do primeiro resistor: "))
R2=int(input("Informe o valor do segundo resistor: "))
R=(R1*R2)/(R1+R2)
print(f"A resistência equivalente é igual a {R} Ohm")
while R1!=0 and R2!=0:
    R1=int(input("Informe o valor do primeiro resistor: "))
    R2=int(input("Informe o valor do segundo resistor: "))
    R=(R1*R2)/(R1+R2)
    print(f"A resistência equivalente é igual a {R} Ohm")
else:
    print("Fim!")