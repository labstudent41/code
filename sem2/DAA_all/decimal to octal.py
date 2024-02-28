import timeit
n=int(input("enter the no"))
m=n
stack=[]
while n!=0:
    rem=n%8
    stack.append(rem)
    n=n//8
    result=""
l=len(stack)
l=l-1
while l>=0:
    result+=str(stack[l])
    l=l-1
print("the given no. is",m)
print("octal equivalent",result)
print("running time",timeit.timeit())
