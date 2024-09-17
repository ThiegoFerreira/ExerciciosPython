def salario(salario,horas):
    if horas>40:
        h= horas - 40
        pct=(h*50)/100
        pct2=pct*salario
        res= salario+ pct2
        return res
    elif horas <=40:
        res=salario
        return res

sl= int(input("Digite o salario: "))
hr= int(input("Digite as horas trabalhadas na semana: "))

print(f'O sálario de R${sl:.2f} referente as {hr} horas trabalhadas é de {salario(sl,hr):.2f}')