alt = float(input("Informe a sua altura: "))
sexo = input("Informe M para o sexo masculino ou F para feminino:")
if sexo == "M":
    print("O peso ideal é", alt*72.7-58)
else:
    print("O peso ideal é", alt*62.1-44.7)