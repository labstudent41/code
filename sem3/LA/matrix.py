
def get_input(X, label):
    print("\nEnter values of Matrix %s :-" %label)
    m = int(input("No. of rows    : "))
    n = int(input("No. of columns : "))
    for i in range(m):
        x = []
        for j in range(n):
            x.append(int(input("%s[%d][%d] = " % (label, i+1, j+1))))
        X.append(x)

def show_matrix(X, label):
    print("\nValues of Matrix %s :-" %label)
    for i in range(len(X)):
        for j in range(len(X[0])):
            print(X[i][j], end='\t')
        print()

def add_matrix(A, B):
    X = []
    for i in range(len(A)):
        x = []
        for j in range(len(A[0])):
            x.append(A[i][j] + B[i][j])
        X.append(x)
    return X

def subtract_matrix(A, B):
    X = []
    for i in range(len(A)):
        x = []
        for j in range(len(A[0])):
            x.append(A[i][j] - B[i][j])
        X.append(x)
    return X

def compose_matrix(A, B):
    Am = len(A)
    Bn = len(B[0])
    X = [[0 for i in range(Am)] for j in range(Bn)]
    for i in range(Am):
        for j in range(Bn):
            for k in range(len(B)):
                X[i][j] += A[i][k] * B[k][j]
    return X


# A = [[1, 2],
#      [3, 4]]
# B = [[5, 6],
#      [7, 8]]

A, B = [], []
get_input(A, 'A')
get_input(B, 'B')


show_matrix(A, 'A')
show_matrix(B, 'B')

X = add_matrix(A, B)
show_matrix(X, '(A + B)')

X = subtract_matrix(A, B)
show_matrix(X, '(A - B)')


import numpy as np
if np.linalg.det(A) == 0:
    print("\nMatrix A is Non-Invertible. Inverse doesn't exist.")
else:
    print("\nMatrix A is Invertible. Inverse of A is :-")
    print(np.linalg.inv(A))
 

A = [[1, 2, 3],
     [4, 5, 6]]
B = [[ 4,  1],
     [-1,  3],
     [ 2, -7]]

print()

show_matrix(A, 'A')
show_matrix(B, 'B')

X = compose_matrix(A, B)
show_matrix(X, '(A x B)')
