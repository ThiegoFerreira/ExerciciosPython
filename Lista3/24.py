#  Crie um programa que some todos os números naturais abaixo de 1000 que são múltiplos de 3 
# ou 5.
numeros=[]
for i in range(1,1000):
    if i%3==0 or i%5==0:
        numeros.append(i)
print(sum(numeros))