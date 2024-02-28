def A(s, i):
    print(end="A ---> ")
    if len(s) == i:
        print("Divisible")
    else:
        if s[i] in "0369":
            A(s, i+1)
        elif s[i] in "258":
            B(s, i+1)
        else:
            C(s, i+1)


def B(s, i):
    print(end="B ---> ")
    if len(s) == i:
        print("Not Divisible")
    else:
        if s[i] in "0369":
            B(s, i+1)
        elif s[i] in "258":
            C(s, i+1)
        else:
            A(s, i+1)


def C(s, i):
    print(end="C ---> ")
    if len(s) == i:
        print("Not Divisible")
    else:
        if s[i] in "0369":
            C(s, i+1)
        elif s[i] in "258":
            A(s, i+1)
        else:
            B(s, i+1)


while True:
    A(input("\nEnter a number : "), 0)
