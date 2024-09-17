valor = float(input("Informe o salário atual: "))
tempo = int(input("Informe os anos de serviço: "))

if valor <= 500:
    res = (valor * 0.25) +valor
    if tempo >= 1 and tempo <=3:
        print(f"O novo valor do salário é de {res + 100:.2f}")
    elif tempo >=4 and tempo <= 6:
        print(f"O novo valor do salário é de {res + 200:.2f}")
    elif tempo  >=7 and tempo <= 10:
        print(f"O novo valor do salário é de {res + 300:.2f}")
    elif tempo  >=10:
        print(f"O novo valor do salário é de {res + 500:.2f}")
elif valor > 500 and valor <= 1000:
    res = (valor * 0.20) +valor
    if tempo >= 1 and tempo <=3:
        print(f"O novo valor do salário é de {res + 100:.2f}")
    elif tempo >=4 and tempo <= 6:
        print(f"O novo valor do salário é de {res + 200:.2f}")
    elif tempo  >=7 and tempo <= 10:
        print(f"O novo valor do salário é de {res + 300:.2f}")
    elif tempo  >=10:
        print(f"O novo valor do salário é de {res + 500:.2f}")
elif valor >1000 and valor <= 1500:
    res = (valor * 0.15) +valor
    if tempo >= 1 and tempo <=3:
        print(f"O novo valor do salário é de {res + 100:.2f}")
    elif tempo >=4 and tempo <= 6:
        print(f"O novo valor do salário é de {res + 200:.2f}")
    elif tempo  >=7 and tempo <= 10:
        print(f"O novo valor do salário é de {res + 300:.2f}")
    elif tempo  >=10:
        print(f"O novo valor do salário é de {res + 500:.2f}")
elif valor >1500 and valor <= 2000:
    res = (valor * 0.10) +valor
    if tempo >= 1 and tempo <=3:
        print(f"O novo valor do salário é de {res + 100:.2f}")
    elif tempo >=4 and tempo <= 6:
        print(f"O novo valor do salário é de {res + 200:.2f}")
    elif tempo  >=7 and tempo <= 10:
        print(f"O novo valor do salário é de {res + 300:.2f}")
    elif tempo  >=10:
        print(f"O novo valor do salário é de {res + 500:.2f}")
elif valor >2000:
    if tempo >= 1 and tempo <=3:
        print(f"O novo valor do salário é de {valor + 100:.2f}")
    elif tempo >=4 and tempo <= 6:
        print(f"O novo valor do salário é de {valor + 200:.2f}")
    elif tempo  >=7 and tempo <= 10:
        print(f"O novo valor do salário é de {valor + 300:.2f}")
    elif tempo  >=10:
        print(f"O novo valor do salário é de {valor + 500:.2f}")


    