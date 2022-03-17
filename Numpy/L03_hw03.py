# 2017013736 김찬영
import numpy as np

# Generate two matrixes
a = np.array([[1,2,3],
               [4,5,6],
                [7,8,9]])
b = np.array([[2,2,2],
               [2,2,2],
                [2,2,2]])

# Calculate the result of equations below
#1) a + b
print('1)', a + b) # Addition of each element
#2) a - b
print('2)', a - b) # Subtraction of each element
#3) a * b
print('3)', a * b) # Multiplication of each element
#4) a / b
print('4)', a / b) # Division of each element
#5) a @ b
print('5)', a @ b) # Multiplication of each matrix
#6) a ** 2
print('6)', a ** 2) # Square of each element