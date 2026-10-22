import numpy as np

array = np.array([[1,2,3] , [1,2,3] , [1,2,3]] )
print(array)

print("heres the array :")
print(array[2:5 , 2:5])


array2 = np.arange (0, 9).reshape(3,3)



print(array2)


print("hi")
array4 = np.arange (1, 10).reshape(3,3)
print(array4)


print(array2 * array4)

print(array2 @ array4)