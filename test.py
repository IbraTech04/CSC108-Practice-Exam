def dot_product(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))

def vector_subtraction(v1, v2):
    return [x - y for x, y in zip(v1, v2)]

def scalar_multiply(scalar, vector):
    return [scalar * x for x in vector]

def gram_schmitt_ortho(vectors):
    basis = [vectors[0][:]]
    for v in vectors[1:]:
        ortho = v[:]
        for b in basis:
            # proj(v, u) = dot_product(v, u) / dot_product(u, u) * u
            projection = scalar_multiply(dot_product(v, b) / dot_product(b, b), b)
            ortho = vector_subtraction(ortho, projection)
        basis.append(ortho)
    return basis

vectors = [[2,4,0,4,0,-4], [0,0,3,-4,0,3], [-2,0,0,4,1,-3]]

# x = gram_schmitt_ortho(vectors)

# # print u_1 dot v_3
# # and u_2 dot v_3
# # and u_2 dot u_2
# # where v is the basis and u is in x
# print (dot_product(x[0], vectors[2]))
# print (dot_product(x[1], vectors[2]))
# print (dot_product(x[1], x[1]))


import numpy as np

def orthogonal_projection_matrix(U):
    A = np.array(U).T
    P = np.dot(A, np.linalg.inv(np.dot(A.T, A))).dot(A.T)
    return P

# Example subspace
U = [[1, 1, -1, 1], [7,2,1,4]]

# Calculate the projection matrix
P = orthogonal_projection_matrix(U)

print("Projection Matrix:")
print(P)
