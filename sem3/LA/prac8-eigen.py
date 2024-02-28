import numpy as np

m = [[1, 2],
     [3, 4]]
a, b = np.linalg.eig(m)
print("Eigen value of a : ", a)
print("Eigen value of b :-")
print(b)

m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
a, b = np.linalg.eig(m)
print("Eigen value of a : ", a)
print("Eigen value of b :-")
print(b)
