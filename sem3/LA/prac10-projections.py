import numpy as np

def oprojection(of_vect, on_vect):
    u = np.array(of_vect)
    v = np.array(on_vect)
    scal = np.dot(u, v) / np.dot(v, v)
    vect = scal * v
    return round(scal, 10), np.around(vect, decimals=10)

print(oprojection([2.0, 2.0], [1.0, 0.0]))
print(oprojection([2.0, 2.0], [6.0, 2.0]))
