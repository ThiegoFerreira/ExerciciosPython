alunos=[]
media7=[]
contador=0

while contador <10:
    print("*"*100)
    n1=float(input("Digite a nota 1: "))
    n2=float(input("Digite a nota 2: "))
    n3=float(input("Digite a nota 3: "))
    n4=float(input("Digite a nota 4: "))
    media = (n1+n2+n3+n4)/4
    alunos.append(media)
    if media >=7:
        media7.append(media)
    contador+=1
print(f"O total de alunos com média superior a 7.0 são {len(media7)} alunos.")