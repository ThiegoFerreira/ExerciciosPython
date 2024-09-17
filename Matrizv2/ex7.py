x=[
[11,12,13,21],
[19,18,17,22],
[45,20,27,15],
[16,14,14,29]
]

maior=[]
elementos=0
l=4
c=4
i=0

while i < l:
    j=0
    while j< c:
        aux2=0
        if x[i][j] >20:
            maior.append(x[i] [j])
            elementos+=1
        j+=1       
    i+=1

print(f"Total de elementos maior que 20: {elementos}.\nLista dos elementos: {maior}")
