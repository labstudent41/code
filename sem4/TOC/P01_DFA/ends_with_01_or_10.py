def A(s, i):
    print("A->", end=" ")
    if len(s) == i:
        print("Rejected")
    else:
        if s[i] == "0":
            B(s, i+1)
        else:
            D(s, i+1)

def B(s, i):
    print("B->", end=" ")
    if len(s) == i:
        print("Rejected")
    else:
        if s[i] == "0":
            B(s, i+1)
        else:
            C(s, i+1)

def C(s, i):
    print("C->", end=" ")
    if len(s) == i:
        print("Accepted")
    else:
        if s[i] == "0":
            E(s, i+1)
        else:
            D(s, i+1)

def D(s, i):
    print("D->", end=" ")
    if len(s) == i:
        print("Rejected")
    else:
        if s[i] == "0":
            E(s, i+1)
        else:
            D(s, i+1)

def E(s, i):
    print("E->", end=" ")
    if len(s) == i:
        print("Accepted")
    else:
        if s[i] == "0":
            B(s, i+1)
        else:
            C(s, i+1)

# main
while True:
    A(input("\nEnter binary : "), 0)
