nota1 = float(input("Informe a nota do trabalho em laboratório: "))
nota2 = float(input("Informe a nota da avaliação semestral: "))
nota3 = float(input("Informar a nota da avaliação final: "))

# nota1= nota1*2
# nota2=nota2*3
# nota3=nota3*5

# media = (nota1+nota2+nota3)/10
# if media > 0 and media <=2.9:
#     print("Reprovado!")
# elif media >= 3 and media <=5.9:
#     print("Recuperação!")
# elif media >= 6 and media <=10:
#     print("Aprovado!")

if (nota1<0.0 or nota1>10.0) or (nota2<0.0 or \
    nota2> 10.0) or (nota3<0.0 or nota3> 10.0):
    print("Nota inválida")
else:
    media = ((nota1*2)+(nota2*3)+(nota3*5))/10
    print(media)