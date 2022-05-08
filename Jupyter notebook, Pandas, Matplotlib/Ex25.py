# 2017013736 김찬영
# Data Extraction - Indexing

import numpy as np

array1d = np.arange(start=1, stop=10)  # 1~10 array
array1d[0] = 9                          # 0 index : 1  --> 9
array1d[8] = 0                          # 8 index : 10 --> 0
print(type(array1d[0]))                 # type of array[0] index
print(array1d)

array2d = array1d.reshape(3,3)          # 3x3 matrix
print(array2d)

print('(0,0)의 값 :', array2d[0,0])
print('(2,2)의 값 :', array2d[2,2])