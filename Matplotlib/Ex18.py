# 2017013736 김찬영
# Check the following table to implement DataFrame (use'index=')

import pandas as pd

cols = ['Korean', 'Math', 'English', 'Science', 'Economics']        # column's name
lists = [[93, 68, 92, 55, 85], [40, 95, 64, 87, 77], [65, 87, 58, 92, 72]]      # list
indexes = ['TH', 'JD', 'GJ']        # index

dfs = pd.DataFrame(lists, columns=cols, index=indexes)
print(dfs)

dfs.to_csv("./result.csv")      # Create csv with name 'result' from current location (./)