import numpy as np
import subprocess
# Clear screen on Windows
subprocess.run("cls", shell=True)
'''
print('# MCQ1')
arr = np.random.randint(1,101,100).reshape(10,-1)
print(arr)
print(np.shape(arr))

print('# MCQ2')
A = np.array([1,2,3])
B = A*2
print(A)
print(B)

print('# MCQ3')
M = np.eye(4)
R = np.diagonal(M)
B = R.T

print(M)
print(R)
print(np.shape(R))
print(B)
print(np.shape(B))

print('# MCQ8')
ind = np.array([[1,2,3,4],
                [1,2,3,4]])
print(np.argmax(ind))
print(np.argmin(ind))

print('# MCQ9')
ind = np.arange(1,10)
print(ind)
ind = ind.reshape(3,3)
print(ind)
print(ind.trace())

print('# MCQ10')
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
result = np.cross(arr1, arr2)
print(result)
'''
print('# FF3')
A = np.random.randint(1,101,size=(3,3))
B = np.random.randint(1,101,size=(3,3))
print(A)
print(B)
result = np.multiply(A, B)
print(result)