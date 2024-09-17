cod = int(input("Informe o código do produto: "))
qnt = float(input("Informe a quantidade: "))
if cod == 100:
    print(f"O valor do pedido é R${qnt*12.00:.2f}")
elif cod == 102:
    print(f"O valor do pedido é R${qnt*18.50:.2f}")
elif cod == 103:
    print(f"O valor do pedido é R${qnt*25.50:.2f}")
elif cod == 104:
    print(f"O valor do pedido é R${qnt*17.00:.2f}")
elif cod == 105:
    print(f"O valor do pedido é R${qnt*9.50:.2f}")
elif cod == 106:
    print(f"O valor do pedido é R${qnt*6.00:.2f}")
