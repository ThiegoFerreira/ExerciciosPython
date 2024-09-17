peso = float(input("Informe o seu peso: "))
alt = float(input("Informe a sua altura: "))
imc = peso/(alt*alt)
if imc <=18.5:
    print("Sua classificação está abaixo do peso.")
elif imc >=18.6 and imc <= 24.9:
    print("Sua classificação é Saudável.")
elif imc >=25 and imc <= 29.9:
    print("Sua classificação é Peso em Escesso.")
elif imc >=30 and imc <= 34.9:
    print("Sua classificação é Obesidade Grau I")
elif imc >=35 and imc <= 39.9:
    print("Sua classificação é Obesidade Grau II (Severa)")
elif imc >=40:
    print("Sua classificação é Obesidade Grau III (mórbida)")
