a=[[2,3]
   ,[4,5]]

b=[[6,7]
   ,[8,9]]

res=[[0,0],
     [0,0]]

print("Matrix A is: ", a)
print("Matrix B is: ", b)

for i in range(len(a)):
    for j in range(len(a[0])):
        res[i][j]=a[i][j]+b[i][j]

print("The final Matrix is :", res)