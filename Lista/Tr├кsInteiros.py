a = int(input("Digite A: "))
b = int(input("Digite B: "))
c = int(input("Digite C: "))

if a > 0:
    print("Caiu no IF")
    if b > 0 :
        print("Caiu no B")
else:
    print("Caiu no else")
    if c > 0:
        print("Caiu no if do C")