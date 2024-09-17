km = float(input("Digite quantos quilometros percorreu: "))
lt = float(input("Informe quantos litros de combustível usou: "))
res = km/lt
if res < 8:
    print(f"Média: {res:.2f}.Venda o carro!")
elif res>=8 and res<=14:
    print(f"Média: {res:.2f}.Econômico!")
elif res >14:
    print(f"Média: {res:.2f}Super econômico!!!")