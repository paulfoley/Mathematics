import numpy as np

a = np.array([[1,2],[3,4]])
print(a)
# displays the following result:
# array([[1, 2],
#        [3, 4]])

print(np.dot(a,a))
# displays the following result:
# array([[ 7, 10],
#        [15, 22]])

print(a.dot(a)) 
# you can call `dot` directly on the `ndarray`
# displays the following result:
# array([[ 7, 10],
#        [15, 22]])

print(np.matmul(a,a))
# array([[ 7, 10],
#        [15, 22]])