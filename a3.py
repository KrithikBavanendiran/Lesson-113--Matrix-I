a=[[9,10],
   [7,6]]

b=[[5, 4],
   [2,3]]

res=[[0,0],
     [0,0]]

print("Matrix A is: ", a)
print("Matrix B is: ", b)

for i in range(len(a)):
    for j in range(len(a[0])):
        res[i][j]=a[i][j]-b[i][j]

print("The final Matrix is :", res)