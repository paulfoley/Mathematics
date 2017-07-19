# Playground for playing with Linear Algebra concepts

# Import
from decimal import Decimal, getcontext
from vector import Vector
from line import *
from plane import *
from linsys import *

# Get Context
getcontext().prec = 1

'''
# Plus, Minus, Scalar Multiply
vector1 = Vector([8.218,-9.341])
vector2 = Vector([7.119,8.215])
vector3 = Vector([1.671,-1.012,-0.318])
print (vector1.plus(Vector([-1.129,2.111])))
print (vector2.minus(Vector([-8.223,0.878])))
print (vector3.times_scalar(7.41))
'''

'''
# Magnitude and Direction
vector4 = Vector([-0.221, 7.437])
vector5 = Vector([8.813, -1.331, -6.247])
vector6 = Vector([5.581, -2.136])
vector7 = Vector([1.996, 3.108, -4.554])
print (vector4.magnitude())
print (vector5.magnitude())
print (vector6.unit_vector())
print (vector7.unit_vector())
'''

'''
# Dot Product
vector8 = Vector([7.887,4.138])
vector9 = Vector([-5.955,-4.904,-1.874])
print(vector8.dot_product(Vector([-8.802, 6.776])))
print(vector9.dot_product(Vector([-4.496,-8.755,7.103])))

# Angles
vector10 = Vector([3.183,-7.627])
vector11 = Vector([7.35,0.221,5.188])
print(vector10.angle_between_vectors(Vector([-2.668,5.319])))
print(vector11.angle_between_vectors(Vector([2.751,8.259,3.985]), False))
'''

'''
# Parallel and Orthogonal
vector1A = Vector([-7.579,-7.88])
vector2A = Vector([22.737,23.64])
vector1B = Vector([-2.029,9.97,4.172])
vector2B = Vector([-9.231,-6.639,-7.245])
vector1C = Vector([-2.328,-7.284,-1.214])
vector2C = Vector([-1.821,1.072,-2.94])
vector1D = Vector([2.118,4.827])
vector2D = Vector([0,0])
print ("Vectors A:")
print (vector1A.is_parallel_to(vector2A))
print (vector1A.is_orthogonal_to(vector2A))
print ("Vectors B:")
print (vector1B.is_parallel_to(vector2B))
print (vector1B.is_orthogonal_to(vector2B))
print ("Vectors C:")
print (vector1C.is_parallel_to(vector2C))
print (vector1C.is_orthogonal_to(vector2C))
print ("Vectors D:")
print (vector1D.is_parallel_to(vector2D))
print (vector1D.is_orthogonal_to(vector2D))
'''

'''
# Vector Projections
vectorV1 = Vector([3.039,1.879])
vectorB1 = Vector([0.825,2.036])
vectorV2 = Vector([-9.88,-3.264,-8.159])
vectorB2 = Vector([-2.155,-9.353,-9.473])
vectorV3 = Vector([3.009,-6.172,3.692,-2.51])
vectorB3 = Vector([6.404,-9.144,2.759,8.718])

print (vectorV1.component_parallel_to(vectorB1))
print (vectorV2.component_orthogonal_to(vectorB2))
print (vectorV3.component_parallel_to(vectorB3))
print (vectorV3.component_orthogonal_to(vectorB3))
'''

'''
# Cross Products
vectorV1 = Vector([8.462,7.893,-8.187])
vectorW1 = Vector([6.984,-5.975,4.778])
vectorV2 = Vector([-8.987,-9.838,5.031])
vectorW2 = Vector([-4.268,-1.861,-8.866])
vectorV3 = Vector([1.5,9.547,3.691])
vectorW3 = Vector([-6.007,0.124,5.772])

print (vectorV1.cross_product(vectorW1))
print (vectorV2.area_of_parallelogram(vectorW2))
print (vectorV3.area_of_triangle(vectorW3))
'''

'''
# Lines - Parallel, Equal, or Intersection
lineA1 = Line(normal_vector = Vector(['4.046', '2.836']), constant_term = '1.21')
lineA2 = Line(normal_vector = Vector(['10.115', '7.09']), constant_term = '3.025')

lineB1 = Line(normal_vector = Vector(['7.204', '3.182']), constant_term = '8.68')
lineB2 = Line(normal_vector = Vector(['8.172', '4.114']), constant_term = '9.883')

lineC1 = Line(normal_vector = Vector(['1.182', '5.562']), constant_term = '6.744')
lineC2 = Line(normal_vector = Vector(['1.773', '8.343']), constant_term = '9.525')

print ("A Line")
same_line = lineA1.__eq__(lineA2)
print ("Are the same line?: %s" % same_line)
if(not same_line):
    parallel = lineA1.is_parallel_to(lineA2)
    print ("Are Parallel?: %s" % parallel)
    if(not parallel):
        print ("Intersection: %s" % lineA1.intersection(lineA2))

print("B Line")
same_line = lineB1.__eq__(lineB2)
print ("Are the same line?: %s" % same_line)
if(not same_line):
    parallel = lineB1.is_parallel_to(lineB2)
    print ("Are Parallel?: %s" % parallel)
    if(not parallel):
        print ("Intersection: %s" % lineB1.intersection(lineB2))

print ("C Line")
same_line = lineC1.__eq__(lineC2)
print ("Are the same line?: %s" % same_line)
if(not same_line):
    parallel = lineC1.is_parallel_to(lineC2)
    print ("Are Parallel?: %s" % parallel)
    if(not parallel):
        print ("Intersection: %s" % lineC1.intersection(lineC2))
'''

'''
# Planes in 3D
planeA1 = Plane(normal_vector = Vector(['-0.412', '3.806', '0.728']), constant_term = '-3.46')
planeA2 = Plane(normal_vector = Vector(['1.03', '-9.515', '-1.82']), constant_term = '8.65')

planeB1 = Plane(normal_vector = Vector(['2.611', '5.528', '0.283']), constant_term = '4.6')
planeB2 = Plane(normal_vector = Vector(['7.715', '8.306', '5.342']), constant_term = '3.76')

planeC1 = Plane(normal_vector = Vector(['-7.926', '8.625', '-7.212']), constant_term = '-7.952')
planeC2 = Plane(normal_vector = Vector(['-2.642', '2.875', '-2.404']), constant_term = '-2.443')

print ("A Plane:")
print ("Planes Are Equal?: {}".format(planeA1.__eq__(planeA2)))
print ("Planes are Parrallel?: {}".format(planeA1.is_parallel_to(planeA2)))
    
print ("B Plane:")
print ("Planes Are Equal?: {}".format(planeB1.__eq__(planeB2)))
print ("Planes are Parrallel?: {}".format(planeB1.is_parallel_to(planeB2)))

print ("C Plane:")
print ("Planes Are Equal?: {}".format(planeB1.__eq__(planeB2)))
print ("Planes are Parrallel?: {}".format(planeC1.is_parallel_to(planeC2)))
'''

'''
# Linear Systems
p0 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
p1 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
p2 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
p3 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')

s = LinearSystem([p0,p1,p2,p3])
s.swap_rows(0,1)
if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
    print('test case 1 failed')

s.swap_rows(1,3)
if not (s[0] == p1 and s[1] == p3 and s[2] == p2 and s[3] == p0):
    print('test case 2 failed')

s.swap_rows(3,1)
if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
    print('test case 3 failed')

s.multiply_coefficient_and_row(1,0)
if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
    print('test case 4 failed')

s.multiply_coefficient_and_row(-1,2)
if not (s[0] == p1 and
        s[1] == p0 and
        s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
        s[3] == p3):
    print('test case 5 failed')

s.multiply_coefficient_and_row(10,1)
if not (s[0] == p1 and
        s[1] == Plane(normal_vector=Vector(['10','10','10']), constant_term='10') and
        s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
        s[3] == p3):
    print('test case 6 failed')

s.add_multiple_times_row_to_row(0,0,1)
if not (s[0] == p1 and
        s[1] == Plane(normal_vector=Vector(['10','10','10']), constant_term='10') and
        s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
        s[3] == p3):
    print('test case 7 failed')

s.add_multiple_times_row_to_row(1,0,1)
if not (s[0] == p1 and
        s[1] == Plane(normal_vector=Vector(['10','11','10']), constant_term='12') and
        s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
        s[3] == p3):
    print('test case 8 failed')

s.add_multiple_times_row_to_row(-1,1,0)
if not (s[0] == Plane(normal_vector=Vector(['-10','-10','-10']), constant_term='-10') and
        s[1] == Plane(normal_vector=Vector(['10','11','10']), constant_term='12') and
        s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
        s[3] == p3):
    print('test case 9 failed')
'''

# Compute Triangular Form
p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
p2 = Plane(normal_vector=Vector(['0','1','1']), constant_term='2')
s = LinearSystem([p1,p2])
t = s.compute_triangular_form()
if not (t[0] == p1 and
        t[1] == p2):
    print ('test case 1 failed')

p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
p2 = Plane(normal_vector=Vector(['1','1','1']), constant_term='2')
s = LinearSystem([p1,p2])
t = s.compute_triangular_form()
if not (t[0] == p1 and
        t[1] == Plane(constant_term='1')):
    print ('test case 2 failed')

p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
p2 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
p3 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
p4 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')
s = LinearSystem([p1,p2,p3,p4])
t = s.compute_triangular_form()
if not (t[0] == p1 and
        t[1] == p2 and
        t[2] == Plane(normal_vector=Vector(['0','0','-2']), constant_term='2') and
        t[3] == Plane()):
    print ('test case 3 failed')

p1 = Plane(normal_vector=Vector(['0','1','1']), constant_term='1')
p2 = Plane(normal_vector=Vector(['1','-1','1']), constant_term='2')
p3 = Plane(normal_vector=Vector(['1','2','-5']), constant_term='3')
s = LinearSystem([p1,p2,p3])
t = s.compute_triangular_form()
if not (t[0] == Plane(normal_vector=Vector(['1','-1','1']), constant_term='2') and
        t[1] == Plane(normal_vector=Vector(['0','1','1']), constant_term='1') and
        t[2] == Plane(normal_vector=Vector(['0','0','-9']), constant_term='-2')):
    print ('test case 4 failed')

