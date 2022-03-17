# 2017013736 김찬영
import numpy as np

#Generate 15 random integers, 1 to 100. then print the matrix with (3,5) shape.
a = np.random.randint(1,100, size=(3,5))
print('a =', a)

#Print using a
## axis = 0 is row
print('max of a (axis=0) :', a.max(axis=0))
print('min of a (axis=0) :', a.min(axis=0))
print('mean of a (axis=0) :', a.mean(axis=0))
## axis = 1 is column
print('max of a (axis=1) :', a.max(axis=1))
print('min of a (axis=1) :', a.min(axis=1))
print('mean of a (axis=1) :', a.mean(axis=1))