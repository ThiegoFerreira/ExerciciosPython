def temperatura(c):
    F = c * (9.0/5.0) + 32.0
    return F

temp = int(input("Informe a temperatura em graus celsius: "))
f = temperatura(temp)
print(f'{temp} Cº convertido para Fahrenheit: {f} Fº')
