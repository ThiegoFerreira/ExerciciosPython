
numero=0
par=[]
impar=[]
while numero <= 0:
    numero=int(input("Digite um número: "))
    
    for i in range(0,numero+1,1):
        if i%2==0:
            par.append(i)
        else:
            impar.append(i)
print(par)
