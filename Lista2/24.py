op=input("Informe a operação desejada entre, +,-,*,/: ")
num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))

if op =="+":
    res = num1+num2
    print(f"O resultado é {res:.2f}")
elif op =="-":
    res = num1-num2
    print(f"O resultado é {res:.2f}")
elif op =="*":
    res = num1*num2
    print(f"O resultado é , {res:.2f}")
elif op =="/":
    res = num1 / num2
    print(f"O resultado é {res:.2f}")