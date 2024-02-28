def A(s, i):
    print(end="A ---> ")
    if len(s) == i:
        print("String Rejected")
        return
    if s[i] == 'a':
        B(s, i+1)
    else:
        D(s, i+1)

def B(s, i):
    print(end="B ---> ")
    if len(s) == i:
        print("String Accepted")
        return
    if s[i] == "a":
        B(s, i+1)
    else:
        C(s, i+1)

def C(s, i):
    print(end="C ---> ")
    if len(s) == i:
        print("String Rejected")
        return
    if s[i] == "a":
        B(s, i+1)
    else:
        C(s, i+1)

def D(s, i):
    print(end="B ---> ")
    if len(s) == i:
        print("String Accepted")
        return
    if s[i] == "a":
        E(s, i+1)
    else:
        D(s, i+1)

def E(s, i):
    print(end="B ---> ")
    if len(s) == i:
        print("String Rejected")
        return
    if s[i] == "a":
        E(s, i+1)
    else:
        D(s, i+1)

A("aabab", 0)
A("bbabb", 0)
A("ababa", 0)
