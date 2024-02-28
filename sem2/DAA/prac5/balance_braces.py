import timeit


def balance_bracs(expr):
    opened = '(', '[', '{'
    closed = ')', ']', '}'
    stack = []
    for char in expr:
        if char in opened:
            stack.append(char)
            print('pushed', char)
        if char in closed:
            stack.pop(closed.index(char))
            print('popped', char)
    return len(stack) == 0

expr = "(4+2 - 3x[6+7])"
if balance_bracs(expr):
    print('balanced')
else:
    print('not matched')
