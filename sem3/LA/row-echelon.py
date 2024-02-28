m2 = [[1, 2],
      [3, 4]]
m2 = Matrix(m2)
print(m2)

r = m2.rref()
print("Row echelon form")
print(r)

rk = m2.rank()
print("Rank of a matrix")
print(rk)

m3 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]
m3 = Matrix(m3)
print(m3)

r = m3.rref()
print("Row echelon form")
print(r)

rk = m3.rank()
print("Rank of a matrix")
print(rk)
