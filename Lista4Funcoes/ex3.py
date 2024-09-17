def numero(x):
    num=x
    if num < 0:
        return "- 1"
    elif num == 0:
        return "0"
    elif num > 0:
        return "1"
    
num= int(input("Digite um número. O progarama retornará 1 para positivo, -1 para negativo e 0 para igual a zero.: "))
x= numero(num)
print(x)