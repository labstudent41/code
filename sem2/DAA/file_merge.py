def file_merge(file):
    total = 0
    cost = 0
    for i in file:
        total += i
        cost += total
    return cost

def sorted_file_merge(file):
    total = 0
    cost = 0
    file.sort()
    for i in file:
        total += i
        cost += total
    return cost

files = [80, 30, 15, 90, 50]
files = [34, 12, 65, 7, 35, 20]

import timeit
print("file merge greddy algorithm: ", file_merge(files))
print("Finished in %fs" %timeit.timeit())

import timeit
print("file merge sorting technique: ", sorted_file_merge(files))
print("Finished in %fs" %timeit.timeit())
