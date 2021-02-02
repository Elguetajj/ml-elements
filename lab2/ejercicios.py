import numpy as np

M = np.array([
    [1,1,0,0,0,0,1],
    [0,1,1,0,0,1,0],
    [0,0,1,1,0,0,0],
    [0,0,0,1,1,0,1],
    [1,0,0,0,0,1,1],
    [0,0,0,0,1,1,1],
    [1,1,1,0,0,0,1]
])


M1 = np.array([
    [1,1,0,0,0,1,1],
    [1,1,1,0,1,0,0],
    [0,1,1,1,1,0,0],
    [0,0,1,1,0,0,1],
    [0,1,1,0,1,1,1],
    [1,0,0,0,1,1,1],
    [1,0,0,1,1,1,1]
])


M2 = np.array([
    [1,1,0,0,0,0,0],
    [1,1,0,0,0,0,0],
    [0,0,1,1,0,0,0],
    [0,0,1,1,0,0,0],
    [0,0,0,0,1,1,1],
    [0,0,0,0,1,1,1],
    [0,0,0,0,1,1,1]
])


is_reflexive = lambda matrix: all(np.diagonal(matrix))

print(is_reflexive(M))
print(is_reflexive(M1))
print(is_reflexive(M2))
print("--------------------------------------------------------------")

is_symmetric = lambda matrix: (matrix.transpose() == matrix).all()


print(is_symmetric(M))
print(is_symmetric(M1))
print(is_symmetric(M2))
print("--------------------------------------------------------------")


test = np.array([
    [1,0,1],
    [0,1,0],
    [1,0,1]
])

test2 =  np.array([
    [1,1,1],
    [0,0,1],
    [0,0,1]
])


is_transitive = lambda matrix: ((matrix@matrix)*matrix == matrix@matrix).all()


print(is_transitive(M))
print(is_transitive(M1))
print(is_transitive(M2))
print("--------------------------------------------------------------")

print("A--------------------------------------------------------------")

A = np.arange(5,9).reshape(2,2)
print(A)

print("B--------------------------------------------------------------")
B = np.arange(-7,-1).reshape(2,3)
print(B)

print("C--------------------------------------------------------------")
C = np.arange(4,14,3).reshape(2,2)
print(C)

print("D--------------------------------------------------------------")
D = np.eye(2,dtype=float)
print(D)

print("E--------------------------------------------------------------")
E = np.zeros((2,3),dtype=float)
print(E)

print("H--------------------------------------------------------------")
H = np.vstack((np.hstack((A,D,E)),np.hstack((D,C,B))))

print(H)


