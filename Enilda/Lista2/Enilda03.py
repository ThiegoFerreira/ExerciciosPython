#3 - Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário o valor do saque e depois informar 
# quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo 
# é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota 
pergunta= int(input("Gostaria de realizar um saque? Digite [1] para sim e [2] para sair."))
while pergunta ==1:
    valor=int(input("QUal valor deseja sacar: "))
    if valor >= 10 and valor <=600:
        a=valor%100#resto da divisão do valor a ser sacado pelo valor da nota.
        a1=valor-a#o resto menos o valor a ser sacado
        a2=a1/100#Divisão para saber o número de notas.
        print("valor de a:",a)
        if a2 > 0:
            print(f"Você receberá {a2:.0f} cédulas de R$100.")

        b=a%50
        b1=a-b
        b2=b1/50
        print("Valor de b",b)
        if b2 > 0:
            print(f"Você receberá {b2:.0f} cédulas de R$50.")

        c=b%10
        c1=b-c
        c2=c1/10
        if c2 > 0:
            print(f"Você receberá {c2:.0f} cédulas de R$10.")

        d=c%5
        d1=c-d
        d2=d1/5
        if d2 > 0:
            print(f"Você receberá {d2:.0f} cédulas de R$5.")

        e=d%1
        e1=d-e
        e2=e1/1
        if e2 > 0:
            print(f"Você receberá {e2:.0f} cédulas de R$1.")

    pergunta= int(input("Gostaria de realizar um novo saque saque? Digite [1] para sim e [2] para sair."))