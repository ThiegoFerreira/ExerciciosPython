def argumentosnomeados(param1, **kwargs):
    # print(param1)
    # print(kwargs)
    imp = kwargs['imposto']
    resultado = param1 * imp / 100
    resultado = resultado + kwargs['valor']
    resultado = resultado + (resultado * kwargs['porc']/100)
    texto = f'o {kwargs["nome"]} deve {resultado}'
    return texto

x = argumentosnomeados(1000, imposto = 20, valor = 40, porc = 50, nome = 'Thiago')
print(x)