import timeit

A = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

B = [[1, 1, 1, 2],
     [2, 2, 2, 3],
     [3, 3, 3, 4]]

R = [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            R[i][j] = A[i][k] * B[k][j]

for i in R:
    print(i)
print("Finished in %fs" % timeit.timeit())
