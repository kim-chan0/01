# 2017013736 김찬영
# reshape(-1)

import numpy as np

array1 = np.arange(10)                  # 0~9 array
print(array1)

array2 = array1.reshape(-1,5)           # reshape(-1) is automaticcally create that row or column
print('array2 shape :', array2.shape)

array3 = array1.reshape(5,-1)           #
print('array3 shape :', array3.shape)