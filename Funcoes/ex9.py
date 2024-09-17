from math import floor

def calcularTempo(tempo):
    if tempo <= 15:
        return "Sem valores a cobrar."
    elif tempo > 15 and tempo <=60:
        valor = 9.00
        return valor
    elif tempo > 60:
        hrs = tempo / 60
        arredondamento = floor(hrs)
        valor = 9.00 + (arredondamento * 1.50)
        return valor
    
tempo = int(input("Quantos minutos o veículo permaneceu no estacionamento: "))
valor = calcularTempo(tempo)
print(f'O valor referente aos {tempo} minutos de permanência no estacionamento é de R$: {valor:.2f}')
        
        
        