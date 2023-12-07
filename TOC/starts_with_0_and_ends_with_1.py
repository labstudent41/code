def A(s, i):
    print(end="A ---> ")
    if len(s) == i:
        print("String Rejected")
        return
    if s[i] == '0':
        B(s, i+1)
    else:
        D(s, i+1)

def B(s, i):
    print(end="B ---> ")
    if len(s) == i:
        print("String Rejected")
        return
    if s[i] == '0':
        B(s, i+1)
    else:
        C(s, i+1)

def C(s, i):
    print(end="C ---> ")
    if len(s) == i:
        print("String Accepted")
        return
    if s[i] == '0':
        B(s, i+1)
    else:
        C(s, i+1)

def D(s, i):
    print(end="D ---> ")
    if len(s) == i:
        print("String Rejected")
        return
    if s[i] == '0' or s[i] == '1':
        D(s, i+1)

for s in '1001', '0101', '0000':
    A(s, 0)
