def financiamento(valor,entrada,juros,parcelas):
    valor_sem_entrada = valor - entrada
    mensalidade = valor_sem_entrada / parcelas
    parcela = mensalidade
    contador = 0
    juros_composto=0

    while contador < parcelas:

        parcela+= parcela* (juros/100)
        print(f'Parcela: {parcela:.2f}')
        juros_composto+=parcela
        print(f'Juros composto: {juros_composto:.2f}')
        contador+=1
94,5
99,22


        # juros_composto+=
        # print(taxa)
        # total = mensalidade + (mensalidade * (taxa/100))
    #     print(total)
    # return [valor_sem_entrada, mensalidade, total]


valor=int(input("Informe o valor total do veículo: "))
entrada = int(input("Informe o valor da entrada: "))
juros = int(input("Informe a taxa de juros: "))
parcelas = int(input("Informe a quantidade de parcelas: "))

teste= financiamento(valor,entrada,juros,parcelas)
print(teste)