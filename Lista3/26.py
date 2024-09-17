#  Elabore um algoritmo para fazer cálculo de potenciação. Ou seja, x^y. (Exemplo: 3^4 = 3 x 3 x 3 
# x 3). Seu algoritmo deverá solicitar que o usuário entre com o valor da base (x) e do expoente 
# (y) e apresentar o resultado do cálculo sem utilizar os operadores (por exemplo **). Para 
# resolver o problema utilize estrutura de repetição.

x=int(input("Digite a base da potenciação: "))
y=int(input("Digite o expoente da potenciação: "))
multiplicador=0
potencia=1
contador=0
while contador != y:
   potencia= potencia*x
   contador+=1
    
print(f"O resultado de {x} elevado a {y}º potência é: {potencia}")
