def somaimposto(taxa,custo):
    tx= taxa/100
    tx2= custo*tx
    res= custo+tx2
    return res

taxa = int(input("Qual a porcentagem de imposto: "))
custo = int(input("Qual o valor do produto: "))

print(f'O valor total do produto é: {somaimposto(taxa,custo):.2f}R$.')