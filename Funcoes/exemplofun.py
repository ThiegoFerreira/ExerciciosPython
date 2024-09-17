# def soma(x,y,z):
#     s = x + y + z
#     return s

# res = soma(12,12,12,125)
# print(res)


## *args é uma lista de parâmetros
def somar(num,*args):
    s = num
    i = 0
    # while i < len(args):
    #     s+=args[i]
    #     i+=1        
    for i in args:
        s+=i
    return s


res = somar(11,12,13,14,15)
print(res)



