x = float(input("Informe o valor da venda: "))
res = x * 10/100
res2 = x / 3
res3 = (x-res)*5/100
res4 = x * 5 / 100
print("O valor com o desconto de 10% é",(x -res))
print("O valor de cada parcela ao dividir em 3 vezes é",res2)
print("O valor da comissão de venda em caso de pagamento a vista é",res3)
print("O valor da comissão em caso de venda parcelada é",res4)