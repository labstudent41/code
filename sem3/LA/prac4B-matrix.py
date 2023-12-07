
def show_matrix(x):
    print("Values of matrix A :-")
    for i in range(len(x)):
        for j in range(len(x[0])):
            print(x[i][j], end='\t')
        print()

# identity matrix
A = []
x = int(input("Enter rows and columns : "))
for i in range(x):
    a = []
    for j in range(x):
        if i == j:
            a.append(1)
        else:
            a.append(0)
    A.append(a)

show_matrix(A)

# symmetric matrix
A = []
x = int(input("Enter rows and columns : "))
for i in range(x):
    a = []
    for j in range(x):
        if i <= j:
            a.append(int(input("A[%d][%d] = " %(i+1, j+1))))
        else:
            a.append(A[j][i])
    A.append(a)

show_matrix(A)

## skew-symmetric matrix
A = []
x = int(input("Enter rows and columns : "))
for i in range(x):
    a = []
    for j in range(x):
        if i < j:
            a.append(int(input("A[%d][%d] = " %(i+1, j+1))))
        elif i == j:
            a.append(0)
        else:
            a.append(-A[j][i])
    A.append(a)

show_matrix(A)

import numpy as np

m = np.array([[1, 2], [3, 4]])
v = np.array([3, 2])
print("Matrix vector multiplication : ", np.matmul(m, v))


