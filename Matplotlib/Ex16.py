# 2017013736 김찬영
# DataFrame

import numpy as np
import pandas as pd

cols = ['col1', 'col2', 'col3']     # column's name

list2 = [[1,2,3], [11,12,13]]       # 2D list
df_list2 = pd.DataFrame(list2, columns=cols)

array2 = np.array([[1,2,3],
                    [11,12,13]])     # 2D array
df_array2 = pd.DataFrame(array2, columns=cols)

print(df_list2)
print(df_array2)