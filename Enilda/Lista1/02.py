motorista = input("Informe a placa do seu veículo(Ex: BEE4R22 ou BEE4922): ")
placa = list(motorista)
digito = placa.pop()
if digito == "0" or digito =="1":
    print("Final 0 - 1. Não Circular 2ª Feira.")
elif digito == "2" or digito =="3":
    print("Final 2 - 3. Não Circular 3ª Feira.")
elif digito == "4" or digito =="5":
    print("Final 4 - 5. Não Circular 4ª Feira.")
elif digito == "6" or digito =="7":
    print("Final 6 - 7. Não Circular 5ª Feira.")
elif digito == "8" or digito =="9":
    print("Final 8 - 9. Não Circular 6ª Feira.")

