a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[1,1,1,2],[2,2,2,3],[3,3,3,4]]
result=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range (len(a)):
    for j in range (len(b[0])):
        for k in range (len(b)):
            result[i][j]=result[i][j]+a[i][k]*b[k][j]
for i in result
:
    print(i)

    

