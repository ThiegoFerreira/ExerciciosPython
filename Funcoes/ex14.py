def potencia(pot, tempo):
    consumo = (pot * tempo) / 1000
    return consumo

def conta(consumo, valor):
    fatura = (consumo * valor) * 30
    return fatura

pot = int(input("Informe a potência em Kwh do equipament: "))
tempo = float(input("Informe o tempo de utilização diária: "))
valor= float(input("Informe o valor do Kwh em seu Estado: "))

kwh = potencia(pot, tempo)
valor = conta(kwh, valor)

print(f'O consumo médio diário é de {kwh} Kw/h e o valor estimado na fatura de energia é R$ {valor:.2f}')

