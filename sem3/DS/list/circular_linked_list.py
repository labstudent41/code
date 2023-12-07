class Node:
    def __init__(self, data):
        self.data = data
        self.next = self


class CircularSinglyLinkedList:

    def __init__(self, data=None):
        if data:
            self.tail = Node(data)
        else:
            self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.tail:
            new_node.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
        self.tail = new_node

    def display(self):
        print(end="List[%s] : " % self.count())
        if not self.tail:
            print("Empty")
            return
        current = self.tail.next
        while True:
            print(current.data, end=' -> ')
            current = current.next
            if current == self.tail.next:
                break
        print()

    def search(self, data):
        current = self.tail
        while current:
            current = current.next
            if current.data == data:
                return data
            if current == self.tail:
                return

    def count(self):
        if not self.tail:
            return 0
        current = self.tail
        count = 0
        while True:
            count += 1
            current = current.next
            if current == self.tail:
                return count

    def sort(self):
        if not self.tail:
            print("List is empty")
            return
        current = self.tail.next
        while current:
            smallest = current
            temp = current.next
            while temp != self.tail:
                if temp.data < smallest.data:
                    smallest = temp
                temp = temp.next
            if smallest.data != current.data:
                current.data, smallest.data = smallest.data, current.data
            current = current.next
            if current == self.tail:
                break

    # def reverse(self):
    #     # code by shikha
    #     self.head = self.tail.next
    #     if not self.head:
    #         return
    #     prev = None
    #     current = self.head
    #     next_node = None
    #     while current.next != self.head:
    #         next_node = current.next
    #         current.next = prev
    #         current = next_node
    #     current.next = prev
    #     self.head.next = current
    #     self.head = current

    def reverse(self):
        if not self.tail:
            print("List is empty")
            return
        prev = self.tail
        current = self.tail.next
        while True:
            next_node = current.next
            current.next = prev
            if current == self.tail:
                break
            prev = current
            current = next_node
        self.tail = next_node

    def remove(self, data):
        if not self.tail:
            print("List is empty")
            return

        current = self.tail
        while current.next:
            if current.next == self.tail:
                if current.next.data == data:
                    if current.next == current:
                        self.tail = None
                    else:
                        self.tail = current
                        current.next = current.next.next
                    return data
                break
            if current.next.data == data:
                current.next = current.next.next
                return data
            current = current.next


# main
nums = CircularSinglyLinkedList()

for i in (4, 1, 2, 9, 3):
    nums.append(i)
nums.display()

print("Searching 1, found:", nums.search(1))
print("Searching 7, found:", nums.search(7))

print("Removed : ", nums.remove(3))

print("\nBefore sort")
nums.display()
nums.sort()

print("\nAfter sort")
nums.display()

nums.reverse()
print("\nAfter reverse")
nums.display()
