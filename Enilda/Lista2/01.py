# 1 - O departamento de Educação Física deseja informatizar este setor e colocou à disposição os seguintes dados de 50 alunos: 
# Matrícula, sexo (M, F), altura (cm) e status físico (1–bom, 2–regular, 3–ruim) 
# Estes dados deverão ser lidos através de uma unidade de entrada qualquer. 
# Calcular e imprimir: 
# a) A quantidade de alunos do sexo feminino com altura superior a 170 cm. 
# b) A % de alunos do sexo masculino (em relação ao total de alunos do sexo masculino) cujo status físico seja bom.
cont=0
aluno=[]
while cont<5:
    matricula=int(input("Matricula: "))
    sexo=input("Informe o sexo. M para masculino e F para feminino: ")
    alt=int(input("Informe a altura: "))
    status=int(input("Informe o status fisico. Digite 1 para bom, 2 para regular e 3 para ruim: "))
    cadastro = (matricula,sexo,alt,status)
    aluno.append(cadastro)
    cont+=1
print(aluno)
for sexo,alt in aluno:
    print(sexo,alt)

