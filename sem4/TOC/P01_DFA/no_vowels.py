def A(s, i):
    print("A ---> ", end=" ")
    if len(s) == i:
        print("String Rejected")
    else:
        if s[i] in "aeiou":
            C(s, i+1)
        else:
            B(s, i+1)


def B(s, i):
    print("B ---> ", end=" ")
    if len(s) == i:
        print("String Accepted")
    else:
        if s[i] in "aeiou":
            C(s, i+1)
        else:
            B(s, i+1)


def C(s, i):
    print("C ---> ", end=" ")
    if len(s) == i:
        print("String Rejected")
    else:
        if s[i] in "aeiou":
            C(s, i+1)
        else:
            C(s, i+1)


while True:
    A(input("\nEnter some text : "), 0)
