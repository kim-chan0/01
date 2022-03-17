# 2017013736 김찬영
import numpy as np

# Generate 4x4 matrix 0 to 15
a = np.arange(0,16).reshape(4,4)
print('a =', a)

#Slicing
print('b =', a[:,1])
print('c =', a[2,1:])
print('d =', a[:2,:2])
print('e =', a[1:3,1:3])