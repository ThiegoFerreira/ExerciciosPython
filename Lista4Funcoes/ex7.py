def esfera(x):
    v = (4/3)*3.14159265359 * x
    return v

x = int(input("Informe o raio da esfera: "))
volume = esfera(x)
print(f'{volume} cm3')
