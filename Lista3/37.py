numero = int(input("Digite um número inteiro maior que 1: "))
multiplicador=0
while numero<1:
    numero = int(input("O número deve ser inteiro e maior que 1: "))
for mult in range(2,numero):
    if (numero % mult == 0):
        multiplicador += 1

if(multiplicador==0):
    print("É primo")
else:
    print("Não é primo!")
