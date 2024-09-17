from math import ceil

def calcularTempo(tempo):
    if tempo <= 15:
        return "Sem valores a cobrar."
    elif tempo > 15 and tempo <=60:
        hr = 1
        return hr
    elif tempo > 60:
        hrs = tempo / 60
        arredondamento = ceil(hrs)
        return arredondamento
    
tempo = int(input("Quantos minutos o veículo permaneceu no estacionamento: "))
hr = calcularTempo(tempo)
valor_minimo= 9.00
adicional = hr * 1.50
hr_total = valor_minimo+adicional
pis = hr_total * 0.033
cofins = hr_total * 0.020
icms = hr_total * 0.17
impostos = pis+cofins+icms
total = hr_total + impostos
if tempo <= 15:
    print(calcularTempo(tempo))
elif tempo > 15:
    print(f'Tempo : {hr:.1f} \nPis R$ {pis:.2f}\nCOFINS R$ {cofins:.2f}\nICMS R$ {icms:.2f}\n IMPOSTOS R$ {impostos:.2f}\
          \nTOTAL R$ {total}')
        
        
        