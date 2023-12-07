import timeit
facttable=[1]
def factorial(n):
    try:
        return facttable[n]
    except IndexError:
        if n==0:
            facttable.append(1)
        else:
            facttable.append(n*factorial(n-1))
            return facttable[n]
x=int(input("Enter a number:"))
print(factorial(x))
print("Running time=",timeit.timeit())
