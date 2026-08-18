import numpy as np
import subprocess
# Clear screen on Windows
subprocess.run("cls", shell=True)
# MCQ1
arr = np.random.randint(1,101,100).reshape(10,-1)
print(arr)
print(np.shape(arr))

# MCQ2
A = np.array([1,2,3])
B = A*2
print(A)
print(B)

# MCQ3
M = np.eye(4)
R = np.diagonal(M)
B = R.T

print(M)
print(R)
print(np.shape(R))
print(B)
print(np.shape(B))