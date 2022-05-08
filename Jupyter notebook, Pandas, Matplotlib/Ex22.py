# 2017013736 김찬영
# Ndarray dimension, resize

import numpy as np

array_s1 = np.arange(10)       # 0~9 array
print('array : \n', array_s1)   # \n : enter

array_s2 = array_s1.reshape(2,5)    # transformation 2x5 matrix
print('array_s2 : \n', array_s2)    # \n : enter

array_s3 = array_s2.reshape(5,2)    # transformation 5x2 matrix
print('array_s3 : \n', array_s3)    # \n : enter