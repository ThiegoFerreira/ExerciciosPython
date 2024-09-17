idade = int(input("Informe a idade do nadador: "))
if idade >= 5 and idade <= 12:
    print("Categoria Infantil.")
elif idade >12 and idade <=17:
    print("Categoria Juvenil")
elif idade >= 18:
    print("Categoria Sênior")
else:
    print("Idade insuficiente.")