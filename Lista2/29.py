uf=input("Informe o estado(MG,SP,RJ ou MS): ")
valor=float(input("Informe o valor do produto para calculo de imposto: "))
if uf == "MG":
    total = (valor*0.07)+valor
    print(f"{valor:.2f} + impostos = R${total:.2f}")
elif uf == "SP":
    total = (valor*0.12)+valor
    print(f"{valor:.2f} + impostos = R${total:.2f}")
elif uf == "RJ":
    total = (valor*0.15)+valor
    print(f"{valor:.2f} + impostos = R${total:.2f}")
elif uf == "MS":
    total = (valor*0.08)+valor
    print(f"{valor:.2f} + impostos = R${total:.2f}")    
