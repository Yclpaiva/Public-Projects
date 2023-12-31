import numpy as np

n = np.array(range(101))
m = np.empty([5,3])
print(m)
identity_matrix = np.eye(9)
print('identity matrix',identity_matrix)

arange = np.arange(2,100,2)
print(arange)

#array multiplication
a = np.array([1,3,5,7,9])
b = np.array([1,3,5,7,9])
print(a*b)