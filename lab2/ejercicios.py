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
print("Problem 1--------------------------------------------------------------")
print("Reflexive--------------------------------------------------------------")

print(is_reflexive(M))
print(is_reflexive(M1))
print(is_reflexive(M2))
print("Symmetric--------------------------------------------------------------")

is_symmetric = lambda matrix: (matrix.transpose() == matrix).all()


print(is_symmetric(M))
print(is_symmetric(M1))
print(is_symmetric(M2))


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

print("Transitive--------------------------------------------------------------")

print(is_transitive(M))
print(is_transitive(M1))
print(is_transitive(M2))
print("problem 2--------------------------------------------------------------")

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


print("problem 3--------------------------------------------------------------")


A = np.arange(0,24).reshape(4,6)
print(A)
rota90 = lambda matrix: np.rot90(matrix)
rota180 = lambda matrix: np.rot90(matrix,2)
rota270 = lambda matrix: np.rot90(matrix,3)


print("90--------------------------------------------------------------")
print(rota90(A))
print("180--------------------------------------------------------------")
print(rota180(A))
print("270--------------------------------------------------------------")
print(rota270(A))


rota90_otro_lado = rota270
rota180_otro_lado = rota180
rota270_otro_lado = rota90

print("90_otro_lado--------------------------------------------------------------")
print(rota90_otro_lado(A))
print("180_otro_lado--------------------------------------------------------------")
print(rota180_otro_lado(A))
print("270_otro_lado--------------------------------------------------------------")
print(rota270_otro_lado(A))


print("Problem 4--------------------------------------------------------------")

