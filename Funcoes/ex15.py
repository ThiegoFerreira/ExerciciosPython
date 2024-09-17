def soma(x,*args):
    soma = x
    for i in args:
        soma += i
    return soma

sum= soma(10,10,10)
print(sum)