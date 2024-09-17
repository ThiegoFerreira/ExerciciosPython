nome = input("Digite o nome: ")
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))
n4 = float(input("Digite a nota 4: "))

media = (n1+n2+n3+n4)/4

if media > 7:
    print(f"{nome} aprovado com média {media}.")
elif media <7 and media >= 5:
    print(f"{nome} Recuperação com média {media}.")
else:
    print(f"{nome} REPROVADO(A) com média {media}.")