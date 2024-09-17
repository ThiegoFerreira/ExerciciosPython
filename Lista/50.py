import math

x1= float(input("Informe o ponto x1 do plano cartesiano: "))
y1= float(input("Informe o ponto y1 do plano cartesiano: "))
x2 = float(input("Informe o ponto x2 do plano cartesiano: "))
y2 = float(input("Informe o ponto y2 do plano cartesiano: "))

xx = x1 - x2
yy = y1 - y2
x = xx*xx
y = yy*yy
xy=x+y

res=math.sqrt(xy)

if(res >= 10):
    print("Longe",res)
else:
    print("Perto",res)