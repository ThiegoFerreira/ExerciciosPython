#  Faça um algoritmo que mostre um Menu com opções de um cardápio de restaurante 
# para uma pessoa (Coloque no mínimo 5 opções e máximo 10 opções de cardápio. 
# Ex: Bife acebolado R$15,00; Lasanha R$25,00). A pessoa vai escolher o prato 
# desejado e após escolher o prato, e a quantidade, posteriormente deverá fazer 
# uma pergunta se deseja fazer outro pedido, ao final o algoritmo deverá fazer a
# seguinte pergunta ao usuário, “Aceita pagar a gorjeta do garçom 10% sobre o 
# valor do prato”. Se o usuário aceitar, mostrar o valor final (valor do prato + 10%), 
# caso contrário, mostrar o valor final (somente o valor do prato).  Utilizar Math - Case.

print("","*"*100,"\n","*"*40,"!!!BEM-VINDO!!!", "*"*43,"\n","*"*100)
print("\n"," "*33,"Qual será o pedido de hoje?\n")
print("Cód"," "*6,"Marmitex"," "*20,"Valor")
print("1."," "*7,"Mini"," "*21,"R$18,00")
print("2."," "*7,"Pequeno"," "*18,"R$20,00")
print("3."," "*7,"Médio"," "*20,"R$23,00")
print("4."," "*7,"Grande"," "*19,"R$26,00")
print("5."," "*7,"Fámilia"," "*18,"R$30,00")
valor_total= 0
pedido = int(input("\nPronto para fazer o seu pedido?\nDigite 1 para sim ou digite 2 para não:\n"))

while pedido == 1:
    cod = int(input("Informe o número(cód) do seu pedido: "))
    if cod ==1 or cod ==2 or cod==3 or cod ==4 or cod==5:
        qnt = int(input("\nAgora nos informe a quantidade: "))    
        match cod:
            case 1:
                preco = 18
                parcial=preco*qnt
                valor_total= parcial + valor_total
                print(f"\nSeu pedido é {qnt} marmitex mini no valor de R${parcial:.2f}")
            case 2:
                preco = 20
                parcial=preco*qnt
                valor_total= parcial + valor_total
                print(f"\nSeu pedido é {qnt} marmitex pequeno no valor de R${parcial:.2f}.")
            case 3:
                preco = 23
                parcial=preco*qnt
                valor_total= parcial + valor_total
                print(f"\nSeu pedido é {qnt} marmitex médio no valor de R${parcial:.2f}.")
            case 4:
                preco = 26
                parcial=preco*qnt
                valor_total= parcial + valor_total
                print(f"\nSeu pedido é {qnt} marmitex grande no valor de R${parcial:.2f}.")
            case 5:
                preco = 30
                parcial = preco*qnt
                valor_total= parcial + valor_total
                print(f"\nSeu pedido é {qnt} marmitex fámilia no valor de R${parcial:.2f}.")
    else:
        cod = int(input("\nCódigo inválido. Informe um código válido do cardápio: "))    

    pedido = int(input("\nGostaria de acrescentar mais pedidos?.\nDigite 1 para sim. \nDigite 2 para não."))
gorjeta=input(f"\nO valor total do seu pedido é R${valor_total:.2f}.\nGostaria de contribuir com gorjeta de 10%?\nDigite S para sim e N para não:\n")
if gorjeta == "S":
    valor = (valor_total*0.10)
    total = valor+valor_total
    print(f"\nO valor total de sua compra ficou em R${total:.2f}. \nObrigado pela atenção e volte sempre.")
else:
    print(f"\nO valor total de sua compra ficou em R${valor_total:.2f}.\nObrigado pela atenção e volte sempre.")

