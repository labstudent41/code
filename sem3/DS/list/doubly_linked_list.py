class Node:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        print(self.head.data, self.tail.data)

    def remove(self, data):
        self.display()
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return current.data
            current = current.next
        return False

    breakpoint()
    def remove2(self, data):
        self.display()
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            return data
        if self.head == self.tail:
            return False
        if self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            return data
        current = self.head.next
        while current.next:
            print(current.data, end='\t')
            if current.data == data:
                current.prev.next = current.next
                current.next.prev = current.prev
                return current.data
            current = current.next
        return False

    def display(self):
        current = self.head
        if self.is_empty():
            print("List is Empty")
        while current:
            print(current.data, end=" <----> ")
            current = current.next
        print("NULL")

    def reverse(self):
       prev = None
       current = self.head
       while current:
           next_node = current.next
           current.next = prev
           current.prev = next_node
           prev = current
           current = next_node
       self.head = prev


l = DoublyLinkedList()
for i in range(5):
    l.append(i)
l.display()

# l.reverse()
# l.display()

print("\nRemoving 9...")
print("Removed", l.remove(9))
print("\nRemoving 3...")
print("Removed", l.remove(3))
print("\nRemoving 0...")
print("Removed", l.remove(0))
print("\nRemoving 4...")
print("Removed", l.remove(4))
print("\nRemoving 1...")
print("Removed", l.remove(1))
print("\nRemoving 3...")
print("Removed", l.remove(3))
l.display()
