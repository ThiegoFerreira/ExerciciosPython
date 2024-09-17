pares=0
lidos=0
numero=1
while numero != 0:
    print("*"*100)
    numero=int(input("\nDigite um número inteiro ou digite [0] para sair: "))
    if numero%2==0 and numero!=0:
        pares+=1
        lidos+=1
        print(f"\n{numero} é par.")
    elif numero%2!=0 and numero!=0:
        lidos+=1
        print(f"\n{numero} não é par.")
    print(f"\nNúmeros lidos: {lidos}")
    print(f"\nNúmeros pares: {pares}")
