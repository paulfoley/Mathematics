import numpy as np

m = np.array([[1,2,3],[4,5,6]])
print(m)
# displays the following result:
# array([[1, 2, 3],
#        [4, 5, 6]])

n = m * 0.25
print(n)
# displays the following result:
# array([[ 0.25,  0.5 ,  0.75],
#        [ 1.  ,  1.25,  1.5 ]])

print(m * n)
# displays the following result:
# array([[ 0.25,  1.  ,  2.25],
#        [ 4.  ,  6.25,  9.  ]])

print(np.multiply(m, n))   
# equivalent to m * n
# displays the following result:
# array([[ 0.25,  1.  ,  2.25],
#        [ 4.  ,  6.25,  9.  ]])