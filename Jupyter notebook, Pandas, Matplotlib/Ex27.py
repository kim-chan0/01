# 2017013736 김찬영
# Arithmetic operation

import numpy as np

a = np.array([[1,2,3], [4,5,6]])            # 2x3 matrix
b = np.array([[7,8], [9,10], [11,12]])      # 3x2 matrix

dot_array = np.dot(a,b)                     # a dot b
print(dot_array)