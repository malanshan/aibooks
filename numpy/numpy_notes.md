# numpy

## np.random.shuffle(x)与np.random.permutation(x)
Ref: https://www.cnblogs.com/keye/p/10794322.html

将数组打乱随机排列有两种方法：

* np.random.shuffle(x)：在原数组上进行，改变自身序列，无返回值。
* np.random.permutation(x)：不在原数组上进行，返回新的数组，不改变自身数组。


### 1. np.random.shuffle(x)

(1) 一维数组

```python
import numpy as np

arr = np.arange(10)
print(arr)

np.random.shuffle(arr)
print(arr)
```
打印结果：
```text
[0 1 2 3 4 5 6 7 8 9]

[2 5 7 1 9 3 4 6 0 8]
```


(2) 对多维数组进行打乱排列时，默认是列维度。
```python
import numpy as np
arr = np.arange(12).reshape(3,4)
print(arr)

np.random.shuffle(arr)
print(arr)
```
打印结果：
```text
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
 
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
```

### 2.np.random.permutation(x)
（1）生成一个随机排列的一维数组
```python
arr1 = np.random.permutation(10)
print(arr1)

arr2 = np.random.permutation([0,1,2,3,4,5,6,7,8,9])
print(arr2)
```
打印结果：
```text
[2 9 8 0 4 3 6 5 1 7]
[6 3 0 2 9 8 5 7 4 1]
```

（2）生成随机排列的多维数组
```python
arr3 = np.arange(9).reshape((3, 3))
print(arr3)

arr4 = np.random.permutation(arr3)
print(arr4)
```
打印结果：
```text
[[0 1 2]
 [3 4 5]
 [6 7 8]]
 
[[0 1 2]
 [3 4 5]
 [6 7 8]]
 
[[0 1 2]
 [6 7 8]
 [3 4 5]]
```
可见，np.random.permutation()不改变输入参数数组。