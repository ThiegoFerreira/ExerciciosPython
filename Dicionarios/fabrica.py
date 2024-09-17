fabrica = {}

n=int(input("Digite a quantida de alunos: "))

for i in range(n):
    fabrica[f"aluno{i}"] = input("Digite o nome: ")

for k,v in fabrica.items():
    print(f"{k}: {v}")    