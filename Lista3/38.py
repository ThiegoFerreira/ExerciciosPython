numero = int(input("Digite um número inteiro maior que 1: "))
soma=0
while numero<1:
    numero = int(input("O número deve ser inteiro e maior que 1: "))
for num in range(2,numero):
    print("num",num)
    for i in range(2, num):
        print("i",i)
        multiplicador=0
        if (i % num == 0):
            multiplicador += 1
        elif(multiplicador==0):
            print("soma",soma)
            soma+=i
print(f"A soma dos números primos de 2 até {numero} é {soma}.")
