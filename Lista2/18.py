# numero = int(input('numero: '))
# if numero > 0:
#     soma = 0
#     while numero != 0:
#         resto = numero % 10
#         numero = (numero - resto) // 10
#         soma = soma + resto
#         print(f'soma: {soma}')
# else:
#     print('numero invalido...')

numero = int(input("Digite um número"))

if numero <= 0:
    print("Número inválido")
else:
    aux = str(numero)
    soma = int(aux[0])+ int(aux[1]) + int(aux[2])
    print(soma)