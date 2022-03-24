# 2017013736 김찬영
# DataFrame : Transformation

import numpy as np
import pandas as pd

cols = ['col1', 'col2', 'col3']     # column's name

array2 = np.array([[1,2,3],
                    [11,12,13]])     # 2D array
df_array2 = pd.DataFrame(array2, columns=cols)

array3 = df_array2.values
print('array3 타입 : {}, array3 형태 : {}'.format(type(array3), array3.shape))      # type of array3, shape of array3
print(array3)

list3 = df_array2.values.tolist()      # transformation array -> list
print('list3 타입 : {}'.format(type(list3)))      #type of list3
print(list3)