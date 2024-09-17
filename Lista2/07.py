valor = float(input("Informe o valor de aquisição do produto: "))
valor1= valor+(valor *0.45)
valor2 = valor+(valor *0.30)
if valor < 50.00:
    print("Valor sugerido para revenda é de R$",valor1)
else:
    print("Valor sugerido para revenda é de R$",valor2)