import timeit

def ascending_bubble_sort(data):
    print()

    size = len(data)
    for i in range(size):
        print('Pass', i+1)
        print(data)
        for j in range(i+1, size):
            if data[i] > data[j]:
                temp = data[j]
                data[j] = data[i]
                data[i] = temp

    print()
    return data

def descending_bubble_sort(data):
    print()

    size = len(data)
    for i in range(size):
        print('Pass', i+1)
        print(data)
        for j in range(i+1, size):
            if data[i] < data[j]:
                temp = data[j]
                data[j] = data[i]
                data[i] = temp

    print()
    return data

numbers = [36, 99, 28, 83, -7]
numbers = [5, 9, 3, 12, 19, 7]
print("Numbers before sort: ", numbers)
print("Numbers in ascending order: ",
      ascending_bubble_sort(numbers))
print("Numbers in descending order: ",
      descending_bubble_sort(numbers))

print()
names = ["Ravi", "Natwar", "Vikas"]
print("Names before sort:", names)
print("Names in ascending order: ",
      ascending_bubble_sort(names))
print("Names in descening order: ",
      descending_bubble_sort(names))

print("\nFinished in %fs" % timeit.timeit())
