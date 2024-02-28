def A(s, i, a, b):
    print(end="A ---> ")
    if len(s) == i:
        print("End Of String")
        print("No. of 1s = ", a)
        print("No. of 0s = ", b)
        return
    if s[i] == '0':
        print('a')
        A(s, i+1, a+1, b)
    else:
        print('b')
        A(s, i+1, a, b+1)

while True:
    A(input("\nEnter binary : "), 0, 0, 0)
