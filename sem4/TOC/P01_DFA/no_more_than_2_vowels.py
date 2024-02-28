def A(s, i):
    print(end="A ---> ")
    if len(s) == i:
        print("String Accepted")
        return
    if s[i] in 'aeiou':
        B(s, i+1)
    else:
        A(s, i+1)

def B(s, i):
    print(end="B ---> ")
    if len(s) == i:
        print("String Accepted")
        return
    if s[i] in "aeiou":
        C(s, i+1)
    else:
        B(s, i+1)

def C(s, i):
    print(end="C ---> ")
    if len(s) == i:
        print("String Accepted")
        return
    if s[i] in "aeiou":
        D(s, i+1)
    else:
        C(s, i+1)

def D(s, i):
    print(end="B ---> ")
    if len(s) == i:
        print("String Rejected")
        return
    D(s, i+1)

A("cat", 0)
A("apple", 0)
A("banana", 0)
