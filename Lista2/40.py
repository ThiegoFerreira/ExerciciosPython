a= float(input("Informe o valor de a: "))
b= float(input("Informe o valor de b: "))
c= float(input("Informe o valor de c: "))
delta = (b**2)-(4*a*c)
x1 = (-b+delta**(1/2))/(2*a)
x2 = (-b-delta**(1/2))/(2*a)
if delta < 0:
    print(f"{delta}Não existe raíz")
elif delta ==0:
    if x1>0:
        print(f"{delta}\nExiste uma raíz real que é única{x1}")
    elif x2>0:
        print(f"{delta}\nExiste uma raíz real que é única{x2}")
elif delta >=0:
    print(f"{delta}\nAs duas raízes são {x1} e {x2}.")