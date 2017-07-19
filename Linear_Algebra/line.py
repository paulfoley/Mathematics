## Create a Line Clss

# Imports 
from decimal import Decimal, getcontext
from vector import Vector

# Get Context
getcontext().prec = 1

# Line Class
class Line(object):

    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 2

        if not normal_vector:
            all_zeros = ['0']*self.dimension
            normal_vector = Vector(all_zeros)
        self.normal_vector = normal_vector

        if not constant_term:
            constant_term = Decimal('0')
        self.constant_term = Decimal(constant_term)

        self.set_basepoint()

    def set_basepoint(self):
        try:
            n = self.normal_vector.coordinates
            c = self.constant_term
            basepoint_coords = ['0'] * self.dimension

            initial_index = Line.first_nonzero_index(n)
            initial_coefficient = n[initial_index]

            basepoint_coords[initial_index] = c/initial_coefficient
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Line.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise e

    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not is_initial_term:
                output += '+'

            if not is_initial_term:
                output += ' '

            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))

            return output

        n = self.normal_vector.coordinates

        try:
            initial_index = Line.first_nonzero_index(n)
            terms = [write_coefficient(n[i], is_initial_term=(i==initial_index)) + 'x_{}'.format(i+1)
                     for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
            output = ' '.join(terms)

        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = '0'
            else:
                raise e

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output

    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero():
                return k
        raise Exception(Line.NO_NONZERO_ELTS_FOUND_MSG)

    def is_parallel_to(self, l):
        # Determines if a line is parallel
        n1 = self.normal_vector
        n2 = l.normal_vector
        return n1.is_parallel_to(n2)

    def __eq__(self, l):
        # Determines if a lines are equal
        n1 = self.normal_vector
        n2 = l.normal_vector

        x0 = self.basepoint
        y0 = l.basepoint
        basepoint_difference = x0.minus(y0)

        if n1.is_zero():
            if not n2.is_zero():
                return False
            else:
                diff = self.constant_term - l.constant_term
                return MyDecimal(diff).is_near_zero()
        elif n2.is_zero():
            return False

        if not self.is_parallel_to(l):
            return False

        return basepoint_difference.is_orthogonal_to(n1)

    def intersection(self, l):
        # Computes the intersection of two lines
        n1 = self.normal_vector
        n2 = l.normal_vector

        try:
            A, B = n1.coordinates
            C, D = n2.coordinates
            k1 = self.constant_term
            k2 = l.constant_term
             
            x = (D*k1 - B*k2)/(A*D - B*C)
            y = (A*k2 - C*k1)/(A*D - B*C)

            return Vector([x,y])

        except ZeroDivisionError:
            if self == l:
                return self
            else:
                return None

# My Decimal Class
class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps

