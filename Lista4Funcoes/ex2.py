import calendar

def data(dia,mes,ano):
    d = dia
    m = mes
    a = ano
    if mes == 1:
        m = "janeiro"
    elif mes ==2:
        m = "fevereiro"
    elif mes ==3:
        m = "março"
    elif mes ==4:
        m = "abril"
    elif mes ==5:
        m = "maio"
    elif mes ==6:
        m = "junho"
    elif mes ==7:
        m = "julho"
    elif mes ==8:
        m = "agosto"
    elif mes ==9:
        m = "setembro"
    elif mes ==10:
        m = "outubro"
    elif mes ==11:
        m = "novembro"
    elif mes ==12:
        m = "dezembro"
    print(f"{d} de {m} de {a}")

d = int(input("Digite o dia: "))
m = int(input("Digite o numeral do mês: "))
a = int(input("Digite o ano: "))

imprimir = data(d,m,a)