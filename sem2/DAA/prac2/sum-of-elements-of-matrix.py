import timeit

m = [[10, 11, 12],
     [13, 14, 15],
     [16, 17, 18]]

rows = len(m)
cols = len(m[0])

total = 0
for row in range(rows):
    for col in range(cols):
        total += m[row][col]

print("Sum of elements is", total)
print("Finished in %fs" % timeit.timeit())
