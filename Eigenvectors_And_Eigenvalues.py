# performing eigendecomposition in numpy... 
# importing array and diag from numpy... 
from numpy import array, diag

# importing eig, inv from numpy.linalg... 
from numpy.linalg import eig, inv

# values for A array... 
A = array([
    [1, 2],
    [4, 5]
])

# calculates the eigenvalues and eigenvectors of a square matrix A
eigenvalues, eigenvectors = eig(A)

# prints eigenvalues...
print("\nEIGENVALUES")
print(eigenvalues)

# prints eigenvectors...
print("\nEIGENVECTORS")
print(eigenvectors)

# decomposing and recomposing a matrix in numpy... 
# importing array and diag from numpy... 
from numpy import array, diag

# importing eig, inv from numpy.linalg... 
from numpy.linalg import eig, inv

# values for A array... 
A = array([
    [1, 2],
    [4, 5]
])

# calculates the eigenvalues and eigenvectors of a square matrix A
eigenvalues, eigenvectors = eig(A)

# prints eigenvalues...
print("\nEIGENVALUES")
print(eigenvalues)

# prints eigenvectors...
print("\nEIGENVECTORS")
print(eigenvectors)

# prints rebuild matrix... 
print("\nREBUILD MATRIX")

# Q for eigenvectors value...
Q = eigenvectors

# R for inverse of eigenvectors value...
R = inv(Q)

# create a diagonal matrix from the eigenvalues
L = diag(eigenvalues)

# Q → Matrix of eigenvectors.
# L → Diagonal matrix of eigenvalues.
# R → Inverse of Q (R = np.linalg.inv(Q)).
# @ → Matrix multiplication operator in python.
B = Q @ L @ R 

# print B...
print(B)