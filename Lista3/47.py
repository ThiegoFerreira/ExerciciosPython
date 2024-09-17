# numero=1
# quadrado=0
# soma=0
# for i in range(100):
#     # print("Número: ",numero)
#     quadrado+=numero**2
#     # print(i,"Quadrado", quadrado)
#     soma+=numero
#     # print(i,"soma", soma)
#     numero+=1
# quadrado_soma=soma**2
# resultado= quadrado_soma - quadrado
# print("A diferença é",resultado)

# somadosquadrados=0
# soma=0
# i=1
# while i <=100:
#     somadosquadrados+=i**2
#     soma+=i
#     i+=1
# diferenca =(soma**2) - somadosquadrados
# print(diferenca)

somadosquadrados=soma=0
for i in range(1,101):
    somadosquadrados+=i**2
    soma+=i    
print((soma**2)-somadosquadrados)

