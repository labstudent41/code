import timeit
def insertion_sort(x):
    l=len(x)
    if l<=1:
        return
    for i in range(1,l):
        key=x[i]
        j=i-1
        while j>=0 and key<x[j]:
            x[j+1]=x[j]
            j=j-1
            x[j+1]=key
            print(x)
    


temp=[88,96,73,55,9,23,41]
print("insertion sort original data")
print(temp)
result=insertion_sort(temp)
print("data after sort ")
print(result)
print("time",timeit.timeit)

