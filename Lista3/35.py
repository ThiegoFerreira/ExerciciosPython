vetor=[]
contador=0
while contador<10:
    caractere=input("Digite um caractere: ")
    letra=caractere.upper()
    if letra !="A" and letra != "E" and letra!="I" and letra !="O" and letra !="U":
        vetor.append(letra)
    contador+=1
string=", ".join(vetor)
print(f"O número de consoantes digitadas foi de {len(vetor)}. As consoantes digitadas são: {string}.")

