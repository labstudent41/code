import timeit
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
x=int(input("Enter a number:"))
factorial(x)
print("Running time=",timeit.timeit()
      )
