x=[
[40,30,20],
[17,16,14],
[19,15,18],
]

y=[
[31,32,33],
[21,22,23],
[12,13,19],  
]

z=[]

i=0
l=len(x)
c=len(x[0])

while i < l:
    linha=[]
    j=0
    while j< c:
        soma= x[i][j] + y[i][j]
        linha.append(soma)
        j+=1
    z.append(linha)       
    i+=1

cont=0
while cont < len(x):
    print (z[cont])
    cont+=1
