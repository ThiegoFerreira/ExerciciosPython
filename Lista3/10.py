try:
    n=int(input("Informe o número N: "))
    cont=0
    impar=-1
    while cont < n:
        impar=impar+2
        print(impar)
        cont+=1
except:
    print("Entrada inválida!")