def A(s, i):
    print("A ---> 0")
    if len(s) == i:
        print("End Of String")
    else:
        if s[i] == "a":
            A(s, i+1)
        else:
            B(s, i+1)

def B(s, i):
    print("B ---> 0")
    if len(s) == i:
        print("End Of String")
    else:
        if s[i] == "a":
            C(s, i+1)
        else:
            B(s, i+1)

def C(s, i):
    print("C ---> 0")
    if len(s) == i:
        print("End Of String")
    else:
        if s[i] == "a":
            D(s, i+1)
        else:
            B(s, i+1)

def D(s, i):
    print("D ---> 1")
    if len(s) == i:
        print("End Of String")
    else:
        if s[i] == "a":
            A(s, i+1)
        else:
            B(s, i+1)

while True:
    A(input("\nEnter letters : "), 0)
