
num = int(input("Enter number: "))
index = int(input("Enter power: "))

import timeit

def power(n, p):
    for i in range(p-1):
        n *= n
    return n

print("%d raised to %d is %d" % (num, index, power(num, index)))
print("Finished in %fs" % timeit.timeit())


import timeit

def rpower(n, p):
    if p == 1:
        return n
    else:
        return n * rpower(n, p-1)

print("%d raised to %d is %d" % (num, index, rpower(num, index)))
print("Finished in %fs" % timeit.timeit())
