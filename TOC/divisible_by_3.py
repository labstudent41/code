# unfinished
# doesn't work

def A(s, i):
    print(end="A ---> ")
    if len(s) == i:
        print("Not valid")
        return
    else:
        B(s, i+1)

def B(s, i):
    print(end="B --->")
    if len(s) == i:
        print("Not valid")
        return
    if s[i] == '0' or s[i] == '3' or s[i] == '6' or s[i] == '9':
        C(s, i+1)
    elif s[i] == '1' or s[i] == '4' or s[i] == '7':
        D(s, i+1)
    else:
        E(s, i+1)

def C(s, i):
    print(end="C ---> ")
    if len(s) == i:
        print("Not valid")
        return
    if s[i] == '0' or s[i] == '3' or s[i] == 6 or s[i] == '9':
        F(s, i+1)
    else:
        E(s, i+1)

def D(s, i):
    print(end="D ---> ")
    if len(s) == i:
        return
    if s[i] == '0' or s[i] == '3' or s[i] == 6 or s[i] == '9':
        F(s, i+1)
    else:
        G(s, i+1)

def E(s, i):
    print(end="C ---> ")
    if len(s) == i:
        print("Not valid")
        return
    if s[i] == '0' or s[i] == '3' or s[i] == '4':


for num in '123', '231', '999':
    A(num, 0)
