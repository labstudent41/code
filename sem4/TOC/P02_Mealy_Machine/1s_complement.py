def A(s, i):
    print(end="A ---> ")
    if len(s) == i:
        print("End Of String")
        return
    if s[i] == '0':
        print('1')
        A(s, i+1)
    else:
        print('0')
        A(s, i+1)

while True:
    A(input("Enter Binary : "), 0)
