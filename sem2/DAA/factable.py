factorials = [1]
def factorial(n):
    try:
        return factorials[n]
    except IndexError:
        if n == 0:
            factorials.append(1)
        else:
            factorials.append(n*factorial(n-1))
            return factorials[n]

print(factorial(5))
