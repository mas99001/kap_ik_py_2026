import numpy as np
import subprocess
# Clear screen on Windows
subprocess.run("cls", shell=True)
'''
a = np.array([[1,2,3],[4,5,6]])
print(a)
print("type: ", type(a).__name__)
b = np.zeros(4)
b[0] = 20
print("zeros:", b)
print("ones :", np.ones((2, 3)))
print("range:", np.arange(0, 10, 2))     # start, stop, step
print("lin  :", np.linspace(0, 1, 5))    # 5 evenly spaced points
print("lin  :", np.linspace(0, 100, 9))    # 5 evenly spaced points

m = np.arange(12)
print(m)
m = m.reshape(3,4)
print(m)
print("########################################")
print("shape:", m.shape)
print("ndim :", m.ndim)
print("size :", m.size)
print("dtype:", m.dtype)
print("########################################")
print("element [1, 2]:", m[1, 2])
print("first row    :", m[0])
print("top-left 2x2 :\n", m[:2, :2])
print("########################################")
print("First column\t:", m[:, 0])
print("Second column\t:", m[:, 1])
print("Third column\t:", m[:, 2])
print("last column\t:", m[:, -1])
'''
print("########################################")
prices = np.array([10.0, 20.0, 15.0, 30.0])
qty    = np.array([3, 2, 5, 1])

revenue = prices * qty           # element-wise
print("revenue per item:", revenue)
print("total           :", revenue.sum())
print("average price   :", prices.mean())
print("max revenue     :", revenue.max())

# broadcasting: add 5% tax to every price
print("with tax        :", prices * 1.05)
print("########################################")
a = np.arange(6)
print("flat   :", a)
print("3x2    :\n", a.reshape(3, 2))
print("2x3    :\n", a.reshape(2, 3))
print("transpose of 2x3:\n", a.reshape(2, 3).T)
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
print('# FF3')
A = np.random.randint(1,101,size=(3,3))
B = np.random.randint(1,101,size=(3,3))
print(A)
print(B)
result = np.multiply(A, B)
print(result)
'''

#############
# https://uplevel.interviewkickstart.com/resource/rc-resourcecollection-1861745-3567652-2230-11919-10232689
#############
'''
ar = np.random.randint(1, 101, size=(5, 5))
print("ar:\n", ar)
m = np.mean(ar)
print("mean:", m)
s = np.std(ar)
print("std:", s)
ari = np.eye(5)
print("ari:\n", ari)
ari = ari + 5
print("ari:\n", ari)

a51 = np.random.randint(1, 101, size=(5, 1))
print("a51:\n", a51)
aari = np.multiply(ari, a51)
print("aari:\n", aari)
a33 = np.random.randint(1, 101, size=(3, 3))
b33 = np.random.randint(1, 101, size=(3, 3))
print("a33:\n", a33)
print("b33:\n", b33)
ab33 = np.multiply(a33, b33)
print("ab33:\n", ab33)
import numpy as np
a1000 = np.random.randint(1, 1001, size=(1000, 1000))
cumsum_arr = np.cumsum(a1000)
#print("acumsum:\n", cumsum_arr)
print("10th element:", cumsum_arr[9])
print("100th element:", cumsum_arr[99])
print("500th element:", cumsum_arr[499])

import numpy as np
a1010 = np.random.randint(1, 101, size=(10, 10))
print("a1010:\n", a1010)
min_val = np.min(a1010)
max_val = np.max(a1010)
# min_idx = np.argmin(a1010)
# max_idx = np.argmax(a1010)
min_idx = np.unravel_index(np.argmin(a1010), a1010.shape)
max_idx = np.unravel_index(np.argmax(a1010), a1010.shape)
print("Minimum value:", min_val)
print("Maximum value:", max_val)
print("Index of minimum value:", min_idx)
print("Index of maximum value:", max_idx)
import numpy as np
ar55float = np.random.uniform(0.0, 1.0, size=(5, 5))
print("ar55float:\n", ar55float)

max_idx = np.unravel_index(np.argmax(ar55float), ar55float.shape)
ar55float[max_idx] = 0
print("Modified array:\n", ar55float)
#
import numpy as np
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = A[1:3, 0:2]
#print("B:\n", B)
B[0, 0] = 100
print(A)
#
import numpy as np
arr1d20 = np.random.randint(1, 101, size=20)
print("arr1d20:\n", arr1d20)
even_count = np.sum(arr1d20 % 2 == 0)
odd_count = np.sum(arr1d20 % 2 != 0)
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)
#
import numpy as np
A = np.arange(1, 17).reshape(4, 4)
print("A:\n", A)
B = A[:, ::-1]
print(B)
C = A[::-1, :]
print(C)
'''
import numpy as np
arr8x80border1 = np.ones((8, 8), dtype=int)
arr8x80border1[1:-1, 1:-1] = 0
print("arr8x80border1:\n", arr8x80border1)

