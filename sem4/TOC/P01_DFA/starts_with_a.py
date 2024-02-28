def A(s, i):
    print(end="A ---> ")
    if len(s) == i:
        print("String not accepted")
        return
    if s[i] == 'a':
        B(s, i+1)
    else:
        C(s, i+1)

def B(s, i):
    print(end="B ---> ")
    if len(s) == i:
        print("String accepted")
        return
    if s[i] == 'a' or s[i] == 'b':
        B(s, i+1)

def C(s, i):
    print(end="C ---> ")
    if len(s) == i:
        print("Dead state")
        return
    if s[i] == 'a' or s[i] == 'b':
        C(s, i+1)

#main
x = 'aabb'
A(x, 0)
x = 'baba'
A(x, 0)
x = 'bbbbbbb'
A(x, 0)
