import numpy as np

my_list =[1,2,3,4]
np_array = np.array(my_list)


print(f"my_list: {my_list}")
print(f"np_array: {np_array}")


"""Numpy operations dimensions and shape:
dimensions the nymber of axes or dimension an h=array has use ndi, to get thw
number if the dimesion 
shape: the size of the array in each dimension use shape to gwt the shap 
of ann array"""


np_array = np.array([[1,2],[3,4]])
dimensions = np_array.ndim ## output 2
shape = np_array.shape ## output (2,2)

print(f"shape: {shape}")

print(f"dimensions {dimensions}")



#multi dimensional numpy array

# numpy supports multi dimrensional arrays

multi_dim_array = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

print(f"multi_dim_array: {multi_dim_array}")

#acessing element in the numpy array
# you can acess element in a numpy array using indeiciea;
element = np_array[0,1] ## outpuy 2
print(f"element: {element}")

# arrange : creat an array witha range of values
arr = np.arange(0,10,2) # it will be (0,2,4,6,8)
print(f"arr: {arr}")

#reshape: change the shape of an array without changing its data
reshaped = np_array.reshape(4,1)

print(f"reshaped: {reshaped}")