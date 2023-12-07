def decimal_to_octal(n):
    octal = 0
    while n != 0:
        digit = n % 8
        octal = (octal*10) + digit
        n = n // 8
    return octal

print(decimal_to_octal(10))
