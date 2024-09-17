def pescado(kg):
    if kg <= 50:
        return "Sem multa."
    else:
        excesso = kg - 50
        multa = excesso*4
        return multa

kg = int(input("Informe quantos quilos de pescado: "))
excesso=0
if kg >50:
    excesso += kg - 50
    print(f'O valor da multa a ser pago pelos {excesso} quilos de pescado excedente é R${pescado(kg):.2f}')
elif kg <=50:
    print(pescado(kg))