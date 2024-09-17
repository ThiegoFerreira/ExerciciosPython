import math

num1 = float(input("Informe um número para calcular a raíz quadrada: "))
if num1 > 0:
    print("A raíz quadrada de ",num1," é ",math.sqrt(num1))
else:
    print("Número inválido")
