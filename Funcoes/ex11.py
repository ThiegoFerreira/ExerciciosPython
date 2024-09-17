def imprimir(lista):
    cont = 1
    for item in lista:
        print(f'{cont}, {item}')
        cont+=1
    
def imprimirwhili(lista):
    i = 0
    while i < len(lista):
        print(f'\n{i+1}, {lista[i]}')
        i += 1

lista = ["Abacaxi", "Uva", "Melancia"]

imprimir(lista)