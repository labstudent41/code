
def A(s, i):
    print(end="A ---> ")
    if len(s) == i:
        print("End Of String")
    else:
        if s[i] == "0":
            print("b")
            F(s, i+1)
        else:
            print("b")
            B(s, i+1)


def B(s, i):
    print(end="B ---> ")
    if len(s) == i:
        print("End Of String")
    else:
        if s[i] == "0":
            print("b")
            C(s, i+1)
        else:
            print("b")
            F(s, i+1)


def C(s, i):
    print(end="C ---> ")
    if len(s) == i:
        print("End Of String")
    else:
        if s[i] == "0":
            print("b")
            F(s, i+1)
        else:
            print("b")
            D(s, i+1)


def D(s, i):
    print(end="D ---> ")
    if len(s) == i:
        print("End Of String")
    else:
        if s[i] == "0":
            print("a")
            E(s, i+1)
        else:
            print("b")
            F(s, i+1)


def E(s, i):
    print(end="E ---> ")
    if len(s) == i:
        print("End Of String")
    else:
        if s[i] == "0" or s[i] == "1":
            print("b")
            F(s, i+1)


def F(s, i):
    print(end="F ---> ")
    if len(s) == i:
        print("End Of String")
    else:
        if s[i] == "0":
            print("b")
            F(s, i+1)
        else:
            print("b")
            F(s, i+1)


while True:
    A(input("Enter string : "), 0)
