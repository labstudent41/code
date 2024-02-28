import timeit

class Stack:
    top = -1
    data = []

    def __init__(self, size):
        self.size = size

    def isFull(self):
        return self.top == self.size - 1

    def isEmpty(self):
        return self.top < 0

    def push(self, x):
        if self.isFull():
            print("Stack Overflow")
        else:
            self.top += 1
            self.data.append(x)

    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
        else:
            print("Popped item '%s' from postition '%d'" %
                  (self.data.pop(), self.top))
            self.top -= 1

    def show(self):
        for i in range(self.top+1):
            print(self.data[i])

stack = Stack(5)

stack.push("Samsung")
stack.push("Vivio")
stack.push("Pixel")
stack.push("Xiomi")
stack.push("nokia")

print()
stack.show()
print()

stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()

print("Finished in %fs" % timeit.timeit())
