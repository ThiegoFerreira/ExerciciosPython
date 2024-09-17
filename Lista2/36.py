valor = float(input("Informe o valor do custo do fabricante: "))
if valor >0 and valor <=12000:
    res = (valor *0.05) + valor
    print(f"O custo para o conumidor é de R${res:.2f}")
elif valor >12000 and valor <=25000:
    res = (valor*0.25) + valor
    print(f"O custo para o consumidor é de R${res:.2f}")
elif valor > 25000:
    res = (valor*0.35) + valor
    print(f"O valor para o consumidor é de R${res:.2f}")
