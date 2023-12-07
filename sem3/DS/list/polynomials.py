class Node:
    def __init__(self, coef, expo):
        self.coef = coef
        self.expo = expo
        self.next = None


def add_polynomial(p1, p2):
    result = Node(0, 0)
    current = result
    while p1 and p2:
        if p1.expo > p2.expo:
            current.next = Node(p1.coef, p1.expo)
            p1 = p1.next
        elif p1.expo < p2.expo:
            current.next = Node(p2.coef, p2.expo)
            p2 = p2.next
        else:
            coef_sum = p1.coef + p2.coef
            if coef_sum != 0:
                current.next = Node(coef_sum, p1.expo)
                p1 = p1.next
                p2 = p2.next
        current = current.next
    while p1:
        current.next = Node(p1.coef, p1.expo)
        p1 = p1.next
        current = current.next
    while p2:
        current.next = Node(p2.coef, p2.expo)
        p2 = p2.next
        current = current.next
    return result.next


# def sort_polynomial(p):
#     # code by pinky
#     res = Node(0, 0)
#     curr = res
#     temp = p
#     while p is not None:
#         temp = p.next
#         if p.expo > temp.expo:
#             curr.next = Node(p.coe, p.expo)
#             p = p.next
#         else:
#             p = p.next
#             curr.next = Node(p.coe, p.expo)
#         curr = curr.next
#     return res.next


def print_polynomial(p1):
    current = p1
    while current:
        if current.next:
            print(f"{current.coef}x^{current.expo}", end="+")
        else:
            print(f"{current.coef}x^{current.expo}")
        current = current.next


# main
p1 = Node(3, 2)
p1.next = Node(2, 1)
p1.next.next = Node(5, 0)

p2 = Node(4, 3)
p2.next = Node(1, 1)

p3 = add_polynomial(p1, p2)
print("Result after addition")
print_polynomial(p3)
