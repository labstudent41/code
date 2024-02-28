def A(s, i):
    print("A ---> 0")
    if len(s) == i:
        print("End Of String")
        return
    if s[i] == "a":
        A(s, i+1)
    else:
        B(s, i+1)

def B(s, i):
    print("B ---> 0")
    if len(s) == i:
        print("End Of String")
        return
    if s[i] == "a":
        A(s, i+1)
    else:
        C(s, i+1)

def C(s, i):
    print("C ---> 1")
    if len(s) == i:
        print("BYE")
        return
    if s[i] == "a":
        A(s, i+1)
    else:
        C(s, i+1)

while True:
    A(input("\nEnter Letters : "), 0)
