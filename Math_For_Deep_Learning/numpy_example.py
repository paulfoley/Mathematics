## Practice Using Numpy

# Imports
import numpy as np

# Functions
def prepare_inputs(inputs):
    input_array = np.array([inputs])
    
    inputs_minus_min = input_array - np.min(input_array)

    inputs_div_max = inputs_minus_min / np.max(inputs_minus_min)

    return input_array, inputs_minus_min, inputs_div_max
    
def multiply_inputs(m1, m2):
    shape_1 = m1.shape
    shape_2 = m2.shape
    if shape_1[0] != shape_2[1] and shape_1[1] != shape_2[0] :
        return False
    elif shape_1[1] == shape_2[0]:
        return np.matmul(m1, m2)  
    elif shape_1[0] == shape_2[1]:
        return np.matmul(m2, m1)
    
def find_mean(values):
    return np.mean(values)


# Output
input_array, inputs_minus_min, inputs_div_max = prepare_inputs([-1,2,7])
print("Input as Array: {}".format(input_array))
print("Input minus min: {}".format(inputs_minus_min))
print("Input  Array: {}".format(inputs_div_max))

print("Multiply 1:\n{}".format(multiply_inputs(np.array([[1,2,3],[4,5,6]]), np.array([[1],[2],[3],[4]]))))
print("Multiply 2:\n{}".format(multiply_inputs(np.array([[1,2,3],[4,5,6]]), np.array([[1],[2],[3]]))))
print("Multiply 3:\n{}".format(multiply_inputs(np.array([[1,2,3],[4,5,6]]), np.array([[1,2]]))))

print("Mean == {}".format(find_mean([1,3,4])))