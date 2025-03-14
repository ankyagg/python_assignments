import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print("1D Array:")
print(arr_1d)
print("\n2D Array:")
print(arr_2d)
print("\n3D Array:")
print(arr_3d)

reshaped_2d = arr_1d.reshape(5,1)
print("\nReshaped 1D Array to 2D:")
print(reshaped_2d)

print("\nSlicing 1D Array (First three elements):")
print(arr_1d[:3])

print("\nSlicing 2D Array (First row):")
print(arr_2d[0, :])

print("\nSlicing 3D Array (First 2D matrix):")
print(arr_3d[0, :, :])

print("\nIndexing 1D Array (Element at index 2):")
print(arr_1d[2])

print("\nIndexing 2D Array (Element at row 1, column 2):")
print(arr_2d[1, 2])

print("\nIndexing 3D Array (Element at [1,0,1]):")
print(arr_3d[1, 0, 1])
