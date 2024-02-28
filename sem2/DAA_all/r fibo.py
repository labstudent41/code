import timeit
def rfibo(n):
    if n<=1:
        return 1
    else:
        return rfibo(n-1)+rfibo(n-2)

for i in range(8):
   print(rfibo(i))
print("running time",timeit.timeit())
