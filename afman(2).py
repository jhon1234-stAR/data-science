import numpy as np

#concept of array slicing 
#[start:end;step]

linear_array = np.array([1,2,3,4,5,6,7,8])

print(linear_array[0:3])

print(linear_array[:5])

print(linear_array[::2])## show odd numbers

print(linear_array[::-1])




multi_array = np.array([[1,2,3] , [4,5,6] , [7,8,9]])

print(multi_array)

#slicing in multi dimensional array

print(multi_array[0:2 , 0:2])

print(multi_array[0:2 , 1:3])

print(multi_array[1:3 , 1:2])
############ i do 


array = np.array([[1,2,3,4,5,6,7,] , [1,2,3,4,5,6,7,] , [1,2,3,4,5,6,7,] , [1,2,3,4,5,6,7,] , [1,2,3,4,5,6,7,] , [1,2,3,4,5,6,7,] , [1,2,3,4,5,6,7,]])
print(array)


print(array[2:5 , 2:5])




### instead of typing the wholr array you can use np.arrange (0, (number of your choice on how many boxes you use))
### and reshape (number of rows , number if colums) 


 

k = np.array([1,2,3,4,5,6,7,8,9,10])

even_array = k[k%2==0]

print(even_array)




bool_array=k[k==5]

print(bool_array)

print(k[[5,7]])

print(k[k<5])




print(k[1<k]])