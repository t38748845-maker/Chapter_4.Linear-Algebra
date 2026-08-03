# using sympy to study the inverse and identity matrix... 
# importing * from sympy... 
from sympy import *

# 4x + 2y + 4z = 44
# 5x + 3y + 6z = 56
# 9x + 3y + 6z = 72

# values for matrix...
A = Matrix([
    [4, 2, 4],
    [5, 3, 7],
    [9, 3, 6]
])

# dot product between A and it's inverse...
inverse = A.inv()

# will product identity function... 
identity = inverse * A

# prints inverse matrix...
#([[-1/2, 0, 1/3], [11/2, -2, -4/3], [-2, 1, 1/3]])
print("INVERSE MATRIX: \n{}".format(inverse))

# prints identity matrix...
# ([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print("IDENTITY MATRIX: \n{}".format(identity))

# using numpy to solve a system of equations... 
# importing array from numpy... 
from numpy import array

# importing inv from numpy.linalg... 
from numpy.linalg import inv

# 4x + 2y + 4z = 44
# 5x + 3y + 6z = 56
# 9x + 3y + 6z = 72

# value for A array...
A = array([
    [4, 2, 4],
    [5, 3, 7],
    [9, 3, 6]
])

# value for B array...
B = array([
    44,
    56,
    72
])

# formulate for x, y, z values...
X = inv(A).dot(B)

# prints X...
print(X)

# importing * from sympy... 
from sympy import *

# 4x + 2y + 4z = 44
# 5x + 3y + 6z = 56
# 9x + 3y + 6z = 72

# value for A matrix...
A = Matrix([
    [4, 2, 4],
    [5, 3, 7],
    [9, 3, 6]
])

# value for B matrix...
B = Matrix([
    44,
    56,
    72
])

# formulate matrix value...
X = A.inv() * B

# prints X...
print(X)