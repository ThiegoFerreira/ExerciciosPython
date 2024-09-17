qnt= int(input("Informe a quantidade de provas: "))
contador=0
nota_total=0
while contador<qnt:
    nota=float(input("Informe a nota: "))
    nota_total=nota_total+nota
    contador +=1 
media=nota_total/qnt
print(f"A média do aluno é {media:.1f}")