def A(s, i):
    global num
    print(end="A ---> ")
    if len(s) == i:
        print(num[::-1])
    elif len(s) < 2 or '1' not in s:
        print("String Rejected")
    else:
        if s[i] == '0':
            num += '0'
            A(s, i+1)
        else:
            num += '1'
            B(s, i+1)

def B(s, i):
    global num
    print(end="B ---> ")
    if len(s) == i:
        print(num[::-1])
    elif len(s) < 2 or '1' not in s:
        print("String Rejected")
    else:
        if s[i] == '0':
            num += '1'
            B(s, i+1)
        else:
            num += '0'
            B(s, i+1)

while True:
    num = ''
    binary = input("\nEnter Binary : ")
    A(binary[::-1], 0)
