# x = float(780.000)
# premio1= x * 46 / 100 # *0.46
# premio2 = x * 32 / 100 # * 0.32
# premio3 = x * 22 / 100 # *0.22
# print("No ultimo sorteio, os três ganhadores levaram os prêmio respectivamente de,",premio1,premio2,premio3)

# z = x + premio1
# print(z)

premio = float(input("Digite o valor do prêmio: "))
porc = float(input("Digite a porcentagem: "))
premio = premio + (premio * porc /100)

print(premio)