stack = []

def A(s, i):
    print(end="A ---> ")
    if len(s) == i:
        print("Rejected")
        return
    stack.append(s[i])
    if s[i+1] == '$':
        B(s, i+1)
    else:
        A(s, i+1)

def B(s, i):
    print(end="B ---> ")
    if len(s) == i:
        print("Rejected")
        return
    l = len(stack)
    if stack[l-1] == s[i]:
        stack.pop()
    if s[i+1] == "z":
        C(s, i+1)
    else:
        B(s, i+1)

def C(s, i):
    print(end="C ---> ")
    if len(stack) == 0:
        print("Accepted")
    else:
        print("Rejected")

s1 = 'abac$caabaz'  # accepted
s2 = 'abc$az'  # Rejected
# s = input("Enter the string: ")
A(s1, 0)
A(s2, 0)
