a=input("enter a string")
stack=[ ]
open=["(","[","{"]
close=[")","]","}"]
try:
    for i in a:
        if i in open:
            stack.append(i)
        elif i in close:
            if i=="]":
                if "["==stack[len(stack)-1]:
                    stack.pop()
            elif i==")":
                if "("==stack[len(stack)-1]:
                            stack.pop()
            elif i=="}":
                if "{"==stack[len(stack)-1]:
                            stack.pop()
except IndexError:
    print("stack underflow")
    print("not balanced")
else:
    if len(stack)==0:
        print("balanced")
    else:
        print("not balanced")
                    
