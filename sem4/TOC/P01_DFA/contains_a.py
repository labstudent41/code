def Q0(s, i):
    print(end="Q0 ---> ")
    if len(s) == i:
        print("String not accepted")
        return
    if s[i] == 'a':
        Q1(s, i+1)
    else:
        Q0(s, i+1)

def Q1(s, i):
    print(end="Q1 ---> ")
    if len(s) == i:
        print("String accepted")
        return
    if s[i] == 'a':
        Q1(s, i+1)
    else:
        Q0(s, i+1)

# main
x = 'ababa'
Q0(x, 0)
x = 'bab'
Q0(x, 0)
