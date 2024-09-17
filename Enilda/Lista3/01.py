# 1 - Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados: 

# Código da cidade; 
# Número de veículos de passeio (em 1999); 
# Número de acidentes de trânsito com vítimas (em 1999).  

# Deseja-se saber: 
# Qual o maior e menor índice de acidentes de transito e a que cidade pertence; 
# Qual a média de veículos nas cinco cidades juntas; 
# Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio. 
codigo= int(input("Digite o código da cidade: "))
quantidade = int(input("Digite a quantidade de veículos: "))
acidentes=int(input("Digite a quantidade de acidentes: "))

menor_indice=maior_indice=acidentes
codigo_menor_indice=codigo_maior_indice=codigo
menor_indice=acidentes
codigo_menor_indice=codigo
total_veiculos=quantidade
total_parcial=0
divisor=0
contador=1

while contador <5:
    codigo= int(input("Digite o código da cidade: "))
    quantidade = int(input("Digite a quantidade de veículos: "))
    acidentes=int(input("Digite a quantidade de acidentes: "))
    total_veiculos+=quantidade
    contador+=1
    if acidentes<menor_indice:
        menor_indice = acidentes
        codigo_menor_indice=codigo
    elif acidentes>maior_indice:
        maior_indice=acidentes
        codigo_maior_indice=codigo
    if quantidade < 2000:
        total_parcial+=acidentes
        divisor+=1


print("Total parcial:",total_parcial)
media=(total_veiculos)/5
media2=(total_parcial)/divisor


print(f"\nO menor índice de acidentes pertence a cidade {codigo_menor_indice} com {menor_indice} acidentes.")
print(f"O maior índice de acidentes pertence a cidade {codigo_maior_indice} com {maior_indice} acidentes.")
print(f"\nA média de veículos nas cinco cidades é de {media:.0f}.")
print(f"\nA média de acidentes nas cidades com número de veículos {total_parcial} abaixo de 2000 é {media2:.0f}.")







