# Um funcionário recebe aumento anual. Em 2019 foi contratado por 4000 reais. Em 2020
# recebeu aumento de 1.5%. A partir de 2021, os aumentos sempre correspondem ao dobro do 
# ano anterior. Faça um programa que determine o salário atual do funcionário.

salario =4000
ano=2020
aumento=0.015
while ano <= 2024:
    salario += salario*aumento
    print(ano, aumento)
    aumento *=2
    print(salario)
    ano +=1
