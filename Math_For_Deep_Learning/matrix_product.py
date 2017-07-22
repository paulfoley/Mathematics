import numpy as np

a = np.array([[1,2,3,4],[5,6,7,8]])
print(a)
# displays the following result:
# array([[1, 2, 3, 4],
#        [5, 6, 7, 8]])
print(a.shape)
# displays the following result:
# (2, 4)

b = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(b)
# displays the following result:
# array([[ 1,  2,  3],
#        [ 4,  5,  6],
#        [ 7,  8,  9],
#        [10, 11, 12]])
print(b.shape)
# displays the following result:
# (4, 3)

c = np.matmul(a, b)
print(c)
# displays the following result:
# array([[ 70,  80,  90],
#        [158, 184, 210]])
print(c.shape)
# displays the following result:
# (2, 3)