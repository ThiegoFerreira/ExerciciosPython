valor = float(input("Informe o valor total das vendas referente ao mês: "))
if valor >= 100000.00:
    res= (valor*0.16) + 700.00
    print(f"A comissão de vendas referente ao mês foi de R${res:.2f}")
elif  valor < 100000.00 and valor >= 80000.00:
    res= (valor*0.14) + 650.00
    print(f"A comissão de vendas referente ao mês foi de R${res:.2f}")
elif  valor < 80000.00 and valor >= 60000.00:
    res= (valor*0.14) + 600.00
    print(f"A comissão de vendas referente ao mês foi de R${res:.2f}")
elif  valor<60000.00 and valor >= 40000.00:
    res= (valor*0.14) + 550.00
    print(f"A comissão de vendas referente ao mês foi de R${res:.2f}")
elif  valor <40000.00 and valor>= 20000.00:
    res= (valor*0.14) + 500.00
    print(f"A comissão de vendas referente ao mês foi de R${res:.2f}")
elif  valor < 20000.00 and valor >=0:
    res= (valor*0.14) + 400.00
    print(f"A comissão de vendas referente ao mês foi de R${res:.2f}")