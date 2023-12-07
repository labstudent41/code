import timeit
m1=[[1,2],[3,4],[5,6]]
total=0
r=len(m1)
c=len(m1[0])
for i in range(0,r):
    for j in range(0,c):
        total+=m1[i][j]
print("the total of element",total)
print("running time",timeit.timeit())
