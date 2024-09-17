city=[]
while len(city)<10:
    cidade=input("Informe uma cidade que deseja conhecer: ")
    city.append(cidade)
    city.reverse()
print(f"A sua lista de cidades em ordem decrescente é:\n",city)