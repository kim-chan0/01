# 2017013736 김찬영

# x + y - z = 0
# 2x - y + 3z = 9
# x + 2y + z = 8

import numpy as np
#Generate an matrix that matches the equation.
a = np.array([[1,1,-1],
              [2,-1,3],
               [1,2,1]])
b = np.array([0,9,8])

#Sove the linear algebra.
k = np.linalg.solve(a,b)

#There was an error about 10^-15, so I rounded up to the first decimal.
print('x =', round(k[0],1))
print('y =', round(k[1],1))
print('z =', round(k[2],1))