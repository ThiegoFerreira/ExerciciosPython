# #lista colchetes
# lista = [15,16,17]
# #Tupla parentes
# tupla = ()
# #Dicionario com chaves -> Matriz composta por chaves e valores
# pessoa = {
#     'nome':'Thiego',
#     'idade': 36,
#     'email':'thiagoalmeida@live.com',
#     'fone':'67 9999999999'
# }

# print(pessoa["nome"])
# print(pessoa["idade"])
# print(type(pessoa))
# print(pessoa)

empresa = {
    'razaosocial':'CLARO SA',
    'cidade':'SAO PAULO',
    'estado':'SP',
    'ganhos': 15.99
}
# print(empresa['estado'])
# print(empresa['ganhos'])

for k,v in empresa.items():
    print(f"{k}: {v}")