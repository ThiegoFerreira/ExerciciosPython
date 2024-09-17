tamanho = float(input("Informe o tamanho em m2 da área a ser pintada: "))
litros = tamanho / 6
res1 = litros/18
res2 = litros/3.6
res3 = res1*80
res4 = res2*25
print("A quantidade de litros necessarios é de",litros)
print("A quantidade de galões de 18l necessária é",res1,"e o valor total é R$",res2)
print("A quantidade de galões de 3,6l necessária é",res2,"e o valor total é R$",res4)
