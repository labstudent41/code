def A(s, i):
    if len(s) == i:
        if s[i-1] == '0':
            B(s, i)
        else:
            print("String rejected")
        return
    print(end="A ---> ")
    if s[i] in ('0', '1'):
        A(s, i+1)


def B(s, i):
    print(end="B ---> ")
    if len(s) == i:
        print("String Accepted")
        return


for s in '0010', '1010', '1011':
    A(s, 0)
