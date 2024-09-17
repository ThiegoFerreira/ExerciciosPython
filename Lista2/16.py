salario = float(input("Digite o salário: "))
parcela = float(input("Informe o valor da parcela: "))

if parcela > salario*0.20:
    print("Empréstimo não concedido!")
else:
    print("Empréstimo concedido!")