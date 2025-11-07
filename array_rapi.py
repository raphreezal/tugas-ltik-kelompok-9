'Tugas Numpy'
import numpy as np

arr = np.array([1,2,3,4,5])
print(arr[1])
print(arr[2:5])
print(arr[0] + arr[4])
print(arr)
print(type(arr))

list = [1,2,3,4,5]
print(list)
print(type(list))

a = np.array([1,2,3])
print(np.mean(a))
print(np.sum(a))
print(a * 2)

a1 = np.array([1,2,3,4,5])
a2 = np.array([[1,2],[3,4]])
a3 = np.array([[[1,2,],[3,4]],[[5,6],[7,8]],[[9,10],[11,12]]])

print(a1.ndim)
print(a2.ndim)
print(a3.ndim)

arr = np.array([1,2,3,4,5])
print(arr.dtype)

arr = np.array([1,2,3,4,5], dtype="S")
print(arr)
print(arr.dtype)