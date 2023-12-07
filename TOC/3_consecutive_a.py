def A(s, i):
    print(end="A ---> ")
    if len(s) == i:
        print("String rejected")
        return
    if s[i] == 'a':
        B(s, i+1)
    else:
        A(s, i+1)

def B(s, i):
    print(end="B ---> ")
    if len(s) == i:
        print("Sring accepted")
        return
    if s[i] == 'b':
        A(s, i+1)
    else:
        C(s, i+1)

def C(s, i):
    print(end="C ---> ")
    if len(s) == i:
        print("Sring accepted")
        return
    if s[i] == 'b':
        A(s, i+1)
    else:
        D(s, i+1)

def D(s, i):
    print(end="D ---> ")
    if len(s) == i:
        print("Sring accepted")
        return
    if s[i] == 'a' or s[i] == 'b':
        D(s, i+1)

# main
for s in 'aaabb', 'bbaab', 'abaab':
    A(s, 0)
