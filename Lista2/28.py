idade=int(input("Informe a idade"))
ts=int(input("Informe o tempo de serviço:"))

if idade >= 65 or ts >= 30 or (idade >=60 and ts >=25):
    print("Pode se aposentar!")
else:
    print("Não pode se aposentar")