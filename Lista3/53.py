i=0
imc=0
fem=0
masc=0
alt=0

alturas=0
idade= int(input("Idade: "))
sexo= input("Idade: ")
peso= float(input("Idade: "))
altura= float(input("Idade: "))

maisvelho=idade
maisnovo=idade
maisalto=altura
maisbaixo=altura
maiorpeso=peso


while i<3:
    i+=1
    if idade>maisvelho:
        maisvelho=idade
    if idade<maisnovo:
        maisnovo=idade
    if altura >maisalto:
        maisalto=altura
    if altura <maisbaixo:
        maisbaixo=altura
    if peso > maiorpeso:
        maiorpeso = peso
    
    imc += peso/(altura*altura)

    if sexo =="F" or sexo =="f":
        fem+=1
    if sexo =="M" or sexo =="m":
        masc+=1

    idade= int(input("Idade: "))
    sexo= input("Idade: ")
    peso= float(input("Idade: "))
    altura= float(input("Idade: "))

print(f"Mais velho {maisvelho}")
print(f"Mais novo {maisnovo}")
print(f"Mais alto {maisalto}")
print(f"Mais baixo {maisbaixo}")
print(f"Maior peso {maiorpeso}")
print(f"Mais velho {maisvelho}")
print(f"Mais velho {maisvelho}")

porfem=(fem/i) * 100
pormasc= (masc/i)*100
mediaalturas=alturas/alt
mediaimc=imc/i