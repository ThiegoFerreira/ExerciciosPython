# Crie um programa que leia um número indeterminado de idades de indivíduos (pare quando 
# for informada a idade 0), e calcule a idade média desse grupo.
idade=int(input("Informe a idade ou dgite [0] para sair: "))
total=idade
divisor=1
while idade>0:
    idade=int(input("Informe a idade ou dgite [0] para sair: "))
    if idade!=0:
        total+=idade
        divisor+=1
media = total/divisor
print(f"A média de idade é: {media:.0f}.")