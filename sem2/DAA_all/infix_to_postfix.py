import timeit
operator=['+','-','*','/','(',')','^']
priority={'+':1,'-':1,'*':2,'/':2,'^':3}
def infix_to_postfix(expression):
    stack=[]
    result=" "
    for ch in expression:
        if ch  not in operator:
            result+=ch
        elif ch=='(':
            stack.append("(")
        elif ch==')':
            while stack and stack[-1]!='(':
                result+=stack.pop()
            stack.pop()
        else:
            while stack and stack[-1]!='(' and priority[ch]<=priority[stack[-1]]:
                result+=stack.pop()
            stack.append(ch)
    while stack:
                result=result+stack.pop()
    return result
#main
x=input("Enter the expression:")
print(x)
r=infix_to_postfix(x)
print("postfix: \n",r)
print("time=",timeit.timeit())
