

numeros=[]
par=[]
impar=[]
contador=0
while contador < 20:
    numero=int(input("Digite um número: "))
    numeros.append(numero)
    if numero%2==0:
        par.append(numero)
    elif numero%2!=0:
        impar.append(numero)
    contador+=1

print(f"Todos os números digitados são: {numeros}.")
print(f"Todos os números pares: {par}.")
print(f"Todos os números impares: {impar}")