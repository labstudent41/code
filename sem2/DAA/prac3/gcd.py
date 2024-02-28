import timeit

def rgcd(a, b):
    if b == 0:
        return a
    elif a < b:
        return rgcd(b, a)
    else:
        return rgcd(b, a-b)


n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print("gcd of %d and %d is %d" % (n1, n2, rgcd(n1, n2)))
# print("Finished in %fs" % timeit.timeit())


def rgcd2(a, b):
    if b == 0:
        return a
    else:
        return rgcd(b, a%b)

# print("gcd of %d and %d is %d" % (n1, n2, rgcd2(n1, n2)))


import timeit

def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        return a

print("gcd of %d and %d is %d" % (n1, n2, gcd(n1, n2)))
# print("Finished in %fs" % timeit.timeit())
