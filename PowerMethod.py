import numpy as numpy
# Initialize the matrix
A = numpy.array([[0.9,10.2,0.7],
                [3.3,0.9,1.2],
                [0.01,7.4,2.5]],float)
# Initial Guess                
a = numpy.array([[1],[1],[1]], float)
n = int(input('Maximum Step: '))
eigenvalue = 0
for i in range(n):
    a = A@a
    eigenvalue = numpy.max(a)
    a = a/eigenvalue

print(" eigenvector: \n", a)
print("\n eigenvalue =", eigenvalue)