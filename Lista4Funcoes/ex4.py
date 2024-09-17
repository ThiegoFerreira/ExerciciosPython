def contagem(horas,minutos,segundos):
        h = horas * 60 * 60
        m = minutos * 60
        s = segundos
        total = h + m + s
        return total
h=int(input("Digite as horas: "))
m=int(input("Digite os minutos: "))
s=int(input("Digite os segundos: "))

total=contagem(h,m,s)
print(f'{h} horas, {m} minutos e {s} segundos convertidos em segundo é igual a {total} segundos')