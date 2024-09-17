# lista_vazia = []
# print(type(lista_vazia))

# frutas = ["Mamão", "Banana", "maça", "Pêra"]
# print(frutas[1]) #printar um item da lista(no índice 1)

# numeros = [1,3,5,7,9]
# print(len(numeros))
# print(numeros[2:5])#Slice fatiamento de listas. 

# numeros = [21,98,15,33]
# print(numeros)
# numeros.append(49)#append add no fim da lista
# numeros.append(56)
# numeros.append(27)
# print(numeros)
# numeros.pop()#remove no fim da lista

# numeros = [21,98,15,33,49.90,56,27]
# print(numeros)
# print(len(numeros))
# numeros.pop()
# print(numeros)
# print(len(numeros))
# numeros.insert(2,63)#Insere um número na posição desejada(POSIÇÃO,ITEM)
# print(numeros)
# print(numeros.index(56))#retorna o indice do número.

# numeros = [21,98,15,33,49.90,56,27]
# numeros.sort()#Ordem crescente
# print(numeros)
# numeros.sort(reverse=True)#Ordem descrescente
# print(numeros)

# print(min(numeros))
# print(max(numeros))
# print(sum(numeros))

# media = sum(numeros) / len(numeros)
# print(media)

numeros = [21,98,15,33,49.90,56,27]
numeros.remove(33)
print(numeros)