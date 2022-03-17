# 2017013736 김찬영
import numpy as np # import numpy
c = np.array(range(0,9)) # lenth 9 array from 0

print (c.ndim) # Numer of array dimension
print (c.shape) # Tuple of array dimensions
print (c.size) # Number of elements in the array shape (e.g. (n,m)
print (c.dtype) # Data-type of the array's elements
print (c.itemsize) # Length of one array element in bytes
print (c.data) # Python buffer object pointing to the start of the array's data