def A(s, i):
    print("A ---> 0")
    if len(s) == i:
        print("End Of String")
        return
    if s[i] == "a":
        B(s, i+1)
    else:
        D(s, i+1)

def B(s, i):
    print("B ---> 0")
    if len(s) == i:
        print("End Of String")
        return
    if s[i] == "a":
        C(s, i+1)
    else:
        D(s, i+1)

def C(s, i):
    print("C ---> 1")
    if len(s) == i:
        print("HELLO")
        return
    if s[i] == "a" or s[i] == "b":
        C(s, i+1)

def D(s, i):
    print("D ---> 0")
    if len(s) == i:
        print("End Of String")
        return
    if s[i] == "a" or s[i] == "b":
        D(s, i+1)

while True:
    A(input("\nEnter Letters : "), 0)
