def media(lista):
    med = sum(lista) / len(lista)
    return med

resultado = media([2,9,22,5,78,19,24])
print(f'{resultado:.2f}')