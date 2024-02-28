try:
    a = int(input("Enter dividend: "))
    b = int(input("Enter divisor: "))
    c = a / b
    print(c)
except ZeroDivisionError:
    print("Divisor cannot be zero")
