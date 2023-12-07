import timeit
n=int(input("enter the no"))
m=n
stack=[]
while n!=0:
    rem=n%16
    stack.append(rem)
    n=n//16
    result=""
l=len(stack)
l=l-1
while l>=0:
    result+=str(stack[l])
    l=l-1
if result==10:
    result="A"
if result==11:
    result="B"
if result==12:
    result="C"
if result==13:
    result="D"
if result==14:
    result="E"
if result==15:
    result="F"
print("the given no. is",m)
print("octal equivalent",result)
print("running time",timeit.timeit())
