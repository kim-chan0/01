# 2017013736 김찬영
# Ndarray representation and transformation

import numpy as np

array_int = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(type(array_int))      # type of array_int
print(array_int.dtype)      # datatype of array_int
print(array_int.ndim)       # n-dimension of array_int
print(array_int.shape)      # shape of array_int

array_float = array_int.astype('float')     # transformation of datatype -> astype
print(array_float)
print(array_float.dtype)        # datatype of array_float