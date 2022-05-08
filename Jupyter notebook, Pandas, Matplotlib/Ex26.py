# 2017013736 김찬영
# Data Extraction - Slicing

import numpy as np

array1 = np.arange(start=1, stop=10)    # 1~10 array

array2 = array1[:3]                     # Slicing array
print(array2)
print(type(array2))

array2d = array1.reshape(3,3)           # 3x3 matrix
print(array2d)
print('row : 0~1, col : 0~1 까지의 값 : \n', array2d[0:2, 0:2])
print('row : 1~2, col : 0~3 까지의 값 : \n', array2d[1:3, :])
print('row : 0~1, col : 0 까지의 값 : \n', array2d[:2, 0])