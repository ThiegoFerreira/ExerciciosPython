matrix=[
[3,4,5,6],
[7,6,5,4],
[9,3,2,1],
[1,2,3,4]
]

l=4
c=4
i=0
mult=1
x=0
y=0

while i < l:
    mult*=matrix[x][y]
    x+=1
    y+=1
    i+=1

print(f"O produto dos elementos da diagonal são: {mult}")