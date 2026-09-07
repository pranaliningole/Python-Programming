import numpy as np
arr1 = np.array([1, 2, 3, 4, 5])
print("1D array : ", arr1)
print()

arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("2D array : \n", arr2)
print()

arr3 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print("3D array : \n", arr3)
print()

print(type(arr1))
print(type(arr2))
print(type(arr3))
print()

print("Shape of 1D array : \n", arr1.shape)
print("Shape of 2D arrya : \n", arr2.shape)
print("Shape of 3D arrya : \n", arr3.shape)
print()


print("Dimension of 1D array : \n", arr1.ndim)
print("Dimension of 2D arrya : \n", arr2.ndim)
print("Dimension of 3D arrya : \n", arr3.ndim)
print()

print("Size of 1D array : \n", arr1.size)
print("Size of 2D array : \n", arr2.size)
print("Size of 3D array : \n", arr3.size)
print()