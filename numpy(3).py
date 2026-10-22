import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])


print("normal array:")
print(array)


print("first 5 elements  : ")
print(array[0:5])


print("last 5 elements : ")
print(array[-5:])


print("every 3rd element:")
print(array[::3])

print("reverse order:")
print(array[::-1])




# -----------------------------------------------------------


array2 = np.array([1,2,3,4,5,6,7,8,9,10])

print("normal array:")
print(array2)



print("adding 5 to evey element:")

print("  a : ")
print(array + 5)

print("  b :")
list2 =[]
arrat22 = [1,2,3,4,5,6,7,8,9,10 ]
for i in arrat22:
    list2.append(i+5)
print(list2)
 
print("multipling the numpt array by 3")
print(array2 *3)

print("subracting 2 from every nupy array")
print(array2 - 2 )
