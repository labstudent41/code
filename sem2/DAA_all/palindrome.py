import timeit
s=input("enter a string")
l=len(s)-1
reverse=""

while l>=0:
    reverse+=s[l]
    l=l-1
print("given string",s)
print("reverse",reverse)
if s==reverse:
    print(s,"is palendrome")
else:
    print(s,"is not palendrome")
print("running time",timeit.timeit())

