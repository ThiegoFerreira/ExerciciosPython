numeros=1
quantidade=0
menor=maior=numeros
pares=0
cont_pares=0

while numeros !=0:
    numeros=int(input("Digite um número: "))
    quantidade+=1
    numeros+=numeros
    media=numeros/quantidade
    
    if numeros %2==0:
        pares+=numeros
        cont_pares+=1
        media_pares= pares/cont_pares
    if numeros < menor:
        numeros = menor
    elif numeros > maior:
        numeros = maior
    print(f"A soma dos números digitados é {numeros}.")
    print(f"A quantidade de números digitado é{quantidade}.")
    print(f"A média dos números digitados é {media}.")
    print(f"O mior número digitado é {maior}.")
    print(f"O menor número digitado é {menor}.")
    print(f"A média dos números pares é {media_pares}")
