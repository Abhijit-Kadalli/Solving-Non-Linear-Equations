import numpy as np
import math


# initialize the matrix
A = np.array([[10., -1., 2., 0.],
             [-1., 11., -1., 3.],
             [2., -1., 10., -1.],
             [0.0, 3., -1., 8.]])
# initialize the RHS vector
b = np.array([6., 25., -11., 15.])

N = int(input('Maximum Step: '))
e = float(input('Tolerable Error: '))

print("Linear System:" )
for i in range(A.shape[0]):
    row = ["{}*x{}" .format(A[i, j], j + 1) for j in range(A.shape[1])]
    print(" + ".join(row), "=", b[i])
print()

x = np.zeros_like (b)
for it_count in range(N):
    print("Current solution:" , x)
    x_new = np.zeros_like (x)
    for i in range(A.shape[0]):
        s1 = np.dot(A[i, :i], x[:i])
        s2 = np.dot(A[i, i + 1:], x[i + 1:])
        x_new[i] = (b[i] - s1 - s2) / A[i, i]
    if np.allclose (x, x_new, e, rtol=0.):
        break
    
    x = x_new

print("Solution:" )
print(x)
error = np.dot(A, x) - b
print("Error:" )
print(error)

