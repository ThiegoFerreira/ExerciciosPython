# Faça um programa que some os números ímpares contidos em um intervalo definido pelo 
# usuário. O usuário define o valor inicial do intervalo e o valor final deste intervalo e o programa 
# deve somar todos os números ímpares contidos neste intervalo. Caso o usuário digite um 
# intervalo inválido (começando por um valor maior que o valor final) deve ser escrito uma 
# mensagem de erro na tela, “Intervalo de valores invalido” e o programa´ termina. Exemplo de 
# tela de saída:
# Digite o valor inicial e valor final: 5
# 10
# Soma dos ímpares neste intervalo: 21

numero_inicial=int(input("Digite o valor inicial e o valor final: "))
numero_final=int(input(""))
aux=numero_inicial
impar=0
if numero_inicial<numero_final:
    while aux<numero_final:
        if aux%2!=0:
            impar+=aux
        aux+=1    
    print(f"A soma dos números ímpares no itervalo de {numero_inicial} a {numero_final} é {impar}.")
else:
    print("Intervalo inválido")




