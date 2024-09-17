x = float(input("Informe a quantidade de horas comuns trabalhadas: "))
y = float(input("informe a quantidade de horas extras trabalhadas: "))
res1 = x * 32.50
res2 = y * 44.50
res3 = res1+res2
res4 = res3 *11/100
res5 = res3-res4
print("O salário bruto é:",res3)
print("O sálario liquido descontado 11% é:",res5 )