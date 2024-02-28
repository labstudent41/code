def infix_to_postfix(expr):
    operators = ['+', '-', '/', '*', '^']
    priority = {'+': 1, '-': 1, '/': 2, '*': 2, '^': 3}
    stack = []
    result = ''

    for char in expr:
        print('%-10s  %4s  %-10s' % (result, char, stack))
        if char == '(':
            stack.append(char)

        elif char == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()

        elif char in operators:
            while stack and stack[-1] != '(' and \
                    priority[char] <= priority[stack[-1]]:
                result += stack.pop()
            stack.append(char)

        else:
            result += char

    while stack:
        result += stack.pop()

    return result


# Main
#expr = "a*x^2+b*x+c"
expr = "a+b*c"
print(expr)
print(infix_to_postfix(expr))
