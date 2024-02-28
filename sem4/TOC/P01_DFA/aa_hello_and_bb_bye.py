#print hello when encountered aa & bye when encountered bb

def A(s,i):
    if len(s)==i:
        print("End of String")
        return
    print("A-->")

    if s[i]=="a":
        B(s,i+1)
    else:
        D(s,i+1)
def B(s,i):
    print("B-->")
    if s[i]=="a":
        C(s,i+1)
    else:
        D(s,i+1)
def C(s,i):
    print("C-->")
    print("Hello")
    if len(s)==i:
        print("End of String")
        return
    if s[i]=="a":
        B(s,i+1)
    else:
        D(s,i+1)
def D(s,i):
    print("D-->")

    if len(s)==i:
        print("End of String")
        return
    if s[i]=="b":
        E(s,i+1)
    else:
        B(s,i+1)
def E(s,i):
    print("E-->")
    print("bye")
    if len(s)==i:
        print("End of String")
        return
    if s[i]=="b":
        D(s,i+1)
    else:
        B(s,i+1)

# Main
x="abaabbab"
A(x,0)


