idade = int(input("Informe a idade: "))
teste = input("Teste Aprovado ou Reprovado: ")
prova = float(input("Informe a nota da prova teórica: "))

if (idade >= 18):
    print("Tem idade para tirar CNH")
    if (teste == "Aprovado" and prova >= 7):
        print("Está apto para fazer as aulas práticas! Fim")
    elif(teste == "Reprovado" or prova < 7):
        print("Não está apto para fazer aulas práticas! Fim")
else:
    print("Não tem idade para tirar CNH")