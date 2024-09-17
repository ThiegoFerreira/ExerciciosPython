def maior(x,y,z):
    maior = x
    if y > maior:
        maior = y
    elif z > maior:
        maior = z
    return maior

x = int(input("Digite um número: "))
y = int(input("Digite mais um número: "))
z = int(input("Digite um último número: "))

num = maior(x,y,z)

print(f"dentre os três números o maior é: {num}")
