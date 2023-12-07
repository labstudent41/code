import timeit
def binary_search(x,key):
    l=len(x)
    low=0
    high=l-1
    while low<=high:
        mid=(low+high)//2
        if key<x[mid]:
            high=mid-1
        elif key>x[mid]:
            low=mid+1
        else:
            return mid
    return -1

m=[28,36,55,68,99,105]
search=int(input("enter  a no"))
result=binary_search(m,search)
if result!=-1:
    print("element is present",search)
else:
    print("not present",search)
