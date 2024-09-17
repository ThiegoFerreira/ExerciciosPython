#  Escreva um programa que permita a qualquer aluno introduzir, pelo teclado, uma sequência de 
# notas (válidas no intervalo de 0 a 10) e que mostre na tela, como resultado, a correspondente 
# média aritmética. O número de notas com que o aluno pretenda efetuar o cálculo não
# fornecido ao programa, o qual terminará quando for introduzido um valor que não seja válido
# como nota de aprovação.

nota=float(input("Digite a nota: "))
total=nota
divisor=1
media=total/divisor
print(media)
while nota >=0 and nota <= 10:
    nota=float(input("Digite a nota: "))
    if nota >=0 and nota <=10:
        total+=nota
        divisor+=1
        media=total/divisor
        print(f"Média: {media:.1f}")
print("Fim!")

