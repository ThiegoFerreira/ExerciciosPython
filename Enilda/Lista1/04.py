import math
calculo=input("Gostaria de calcular a quantidade de painéis solares necessários\npara a sua residência? Digite [1] para sim e [2] para não.")
while calculo == "1":
    kwh=float(input("\nCerto. Informe qual a média anual de consumo em KWh da sua residência.\nEsse valor está presente em sua fatura de energia: "))
    potencia = float(input("\nAgora informe a potência da placa solar desejada.\nAs potências variam de, em média, 340w a 560w:"))
    irradiacao_solar=5#média de 5.1 no Brasil
    mensalkw=(irradiacao_solar*potencia*30)/1000#multiplicado por 30 dias e dividido por mil para conversão simples de watts para kw
    res=kwh/mensalkw
    print(f"\nO número necessário de placas solares é {round(res)}")
    calculo=input("\nDeseja fazer um novo cálculo? Digite [1] para sim e [2] para não.")
print("\nObrigado por calcular conosco.")
