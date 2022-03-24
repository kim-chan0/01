# 2017013736 김찬영
# Dimension change using reshape(-1)

import numpy as np

array_8 = np.arange(8)                  # 0~7 array

array3d = array_8.reshape(2,2,2)        #
print('array3d :', array3d.tolist())    # array --> list

array5 = array3d.reshape(-1,1)          # 3d -> 2d
print('array5 :', array5.tolist())      # array --> list
print('array5 shape :', array5.shape)   # shape of array

array6 = array_8.reshape(-1,1)          # 1d -> 2d
print('array6 :', array6.tolist())      # array --> list
print('array6 shape:', array6.shape)    # shape of array