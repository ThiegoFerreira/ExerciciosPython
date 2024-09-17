candidato1=0
candidato2=0
candidato3=0
candidato4=0
voto_nulo=0
voto_branco=0
total=0

escolha=int(input("Gostaria de iniciar a votação? Digite [1] para sim e [2] para sair."))
while escolha==1:
    candidato=int(input("\n[1] Voto em Maria.\n[2] Voto em Mônica.\n[3] Voto em João.\n[4] Voto em Carlos.\n[5] Voto Nulo.\n[6] Voto em Branco.\nDigite a opção desejada: "))
    if candidato==1:
        candidato1+=1
        total+=1
    elif candidato==2:
        candidato2+=1
        total+=1
    elif candidato==3:
        candidato3+=1
        total+=1
    elif candidato==4:
        candidato4+=1
        total+=1
    elif candidato==5:
        voto_nulo+=1
        total+=1
    elif candidato==6:
        voto_branco+=1
        total+=1
    else:
        voto_nulo +=1
    escolha=int(input("Continuar a votação?[1] para sim e [2] para sair."))

porcentagem1= (voto_nulo*100)/total
porcentagem2= (voto_branco*100)/total
print(f"Maria: {candidato1} votos.")
print(f"Mônica: {candidato2} votos.")
print(f"João: {candidato3} votos.")
print(f"Carlos: {candidato4} votos.")
print(f"Total de votos nulos: {voto_nulo} votos.")
print(f"Total de votos em branco: {voto_branco} votos.")
print(f"A porcentagem de votos nulos em realção ao total de votos é de {porcentagem1:.0f}%.")
print(f"A porcentagem de votos em branco em realção ao total de votos é de {porcentagem2:.0f}%.")
# encerrar=1
# while encerrar !=0:
#     encerrar=int(input("Gostaria de encerrar? Digite [0] para sair ou [1] para nova votação"))
#     if encerrar ==1:
#         escolha=int(input("Continuar a votação?[1] para sim e [2] para sair."))