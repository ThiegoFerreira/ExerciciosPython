x = float(input("Informe o número de pãozinhos vendidos: "))
y = float(input("Informe o número de broas vendidos: "))
res1 = x * 0.12
res2 = y * 1.50
res3 = (res1+res2)* 10/100
print("O valor total arrecadado com pãozinhos foi", res1)
print("O valor total arrecadado com broas foi", res2)
print("O valor total a ser alocado em poupança é de",res3)