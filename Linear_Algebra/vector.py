## Create a Vector Class

# Imports
import math
from decimal import Decimal, getcontext

# Get Context
getcontext().prec = 1

# Vector Class
class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def plus(self,v):
        new_coordinates = [x+y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def minus(self,v):
        new_coordinates = [x-y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self, c):
        new_coordinates = [Decimal(c)*x for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return math.sqrt(sum(coordinates_squared))

    def unit_vector(self):
        try:
            return self.times_scalar(1.0/self.magnitude())
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    def dot_product(self, v):
        return sum([x*y for x, y in zip(self.coordinates, v.coordinates)])

    def angle_between_vectors(self, v, radians=True):
        try:
            u1 = self.unit_vector()
            u2 = v.unit_vector()
            angle_in_radians = math.acos(u1.dot_product(u2))
            
            if(radians):
                return angle_in_radians
            else:
                angle_in_degrees = (180. / math.pi) * angle_in_radians
                return angle_in_degrees
        
        except Exception as e:
            raise e

    def is_orthogonal_to(self, v, tolerance = 1e-10):
        return abs(self.dot_product(v)) <= tolerance

    def is_zero(self, tolerance = 1e-10):
        return self.magnitude() < tolerance

    def is_parallel_to(self, v):
        return self.is_zero() or v.is_zero() or self.angle_between_vectors(v) == 0 or self.angle_between_vectors(v) == math.pi

    def get_component(self, basis):
        u = basis.unit_vector()
        weight = self.dot_product(u)
        return u, weight

    def component_parallel_to(self, basis):
        try:
            u, weight = self.get_component(basis)
            return u.times_scalar(weight)
        
        except Exception as e:
            raise e

    def component_orthogonal_to(self, basis):
        try:
            perpendicular_projection = self.component_parallel_to(basis)
            return self.minus(perpendicular_projection)
        
        except Exception as e:
            raise e

    def cross_product(self, v):
        try:
            if (self.dimension == 3 and v.dimension == 3):
                x1, y1, z1 = self.coordinates
                x2, y2, z2 = v.coordinates
                x = ((y1*z2) - (y2*z1))
                y = ((x1*z2) - (x2*z1)) * -1
                z = ((x1*y2) - (x2*y1))
                cross_product = Vector([x,y,z])
                return cross_product
                
        except Exception as e:
            raise e

    def area_of_parallelogram(self, v):
        return self.cross_product(v).magnitude()

    def area_of_triangle(self, v):
        area_of_parallelogram = self.area_of_parallelogram(v)
        return area_of_parallelogram / 2.0

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates