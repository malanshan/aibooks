#!/usr/bin/python3
# coding=utf-8


import numpy as np

arr = np.arange(10)
print(arr)

np.random.shuffle(arr)
print(arr)

arr = np.arange(12).reshape(3,4)
print(arr)

np.random.shuffle(arr)
print(arr)


arr = np.random.permutation(10)
print(arr)

arr2 = np.random.permutation([0,1,2,3,4,5,6,7,8,9])
print(arr2)


arr3 = np.arange(9).reshape((3, 3))
print(arr3)

arr4 = np.random.permutation(arr3)
print(arr3)
print(arr4)
