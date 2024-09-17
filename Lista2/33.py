valor = float(input("Informe o valor do produto:"))
if valor < 50:
    res = (valor * 0.05) + valor
    print(f"O valor de R${valor:.2f} com acrescimo de 5% de reajuste fica R${res:.2f}.")
elif valor >= 50 and valor <100:
    res = (valor*0.10) + valor
    print(f"O valor de R${valor:.2f} com acrescimo de 10% de reajuste fica R${res:.2f}.")
elif valor >= 100:
    res = (valor * 0.15) + valor
    print(f"O valor de R${valor:.2f} com acrescimo de 15% de reajuste fica R${res:.2f}.")