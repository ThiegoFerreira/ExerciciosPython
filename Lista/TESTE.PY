produto1 = input("Digite o nome do produto:")
qnt1 = int(input(f"Digite a quantidade de {produto1}"))
produto2 = input("Digite o nome do produto:")
qnt2 = int(input(f"Digite a quantidade de {produto2}"))
produto3 = input("Digite o nome do produto:")
qnt3 = int(input(f"Digite a quantidade de {produto3}"))
print(f"A quantidade de {produto1} é {qnt1}.")
print(f"A quantidade de {produto2} é {qnt2}.")
print(f"A quantidade de {produto3} é {qnt3}.")
venda1 = input("Venda ou compra? ")
venda=str
compra = str
if(venda1 == venda): 
    decisao = input("Qual o produto vendido? ")
    if(decisao == produto1):
        qnt_venda1 = int(input(f"Digite a quantidade de {produto1} vendidos: "))
        saldo_produto1 = qnt1 - qnt_venda1
        print(f"Saldo atual de {produto1} é {saldo_produto1}")
        if(decisao == produto2):
            qnt_venda2 = int(input(f"Digite a quantidade de {produto2} vendidos: "))
            saldo_produto2 = qnt1 - qnt_venda2
            print(f"Saldo atual de {produto2} é {saldo_produto2}")
            if(decisao == produto3):
                qnt_venda3 = int(input(f"Digite a quantidade de {produto3} vendidos: "))
                saldo_produto3 = qnt1 - qnt_venda3
                print(f"Saldo atual de {produto3} é {saldo_produto3}")
                add = input("Digite o nome do produto adicionado: ")
                if(add == produto1):
                    qnt_add = int(input(f"Digite a quantidade de {produto1} adicionados"))
                    saldo_produtoadd = saldo_produto1 + qnt_add
                    print(f"Saldo atual de {produto1} é {saldo_produtoadd}")
                    if(add == produto2):
                        qnt_add2 = int(input(f"Digite a quantidade de {produto2} adicionados"))
                        saldo_produtoadd2 = saldo_produto1 + qnt_add2
                        print(f"Saldo atual de {produto2} é {saldo_produtoadd2}")
                        if(add == produto3):
                            qnt_add3 = int(input(f"Digite a quantidade de {produto3} adicionados"))
                            saldo_produtoadd3 = saldo_produto3 + qnt_add3
                            print(f"Saldo atual de {produto3} é {saldo_produtoadd3}")

