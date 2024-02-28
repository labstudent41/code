def A(s, i):
    print(end="A ---> ")
    if len(s) == i:
        print("String Rejected")
        return
    if s[i] == "1":
        A(s, i+1)
    else:
        B(s, i+1)

def B(s, i):
    print(end="B ---> ")
    if len(s) ==  i:
        print("String Accepted")
        return
    if s[i] == "1":
        A(s, i+1)
    else:
        B(s, i+1)

for s in '0010', '1010', '1011':
    A(s, 0)
