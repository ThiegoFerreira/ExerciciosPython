base1= float(input("Informe a base mair do trapézio: "))
base2= float(input("Informe a base menor do trapézio: "))
alt=float(input("Informe a altura do trapézio: "))

area = ((base1+base2)*alt)/2

if base1 > 0 and base2 >0:
    print("A área do trapézio é", area,"m2.")
else:
    print("Número inválido")