import subprocess as sb
sb.run("cls", shell=True)
print("------------------------------------")
print("Welcome to the OOP Assignment 04-PRE")
print("------------------------------------")
import numpy as np
class Numpydemo:
    def __init__(self, array):
        self.array = array

    def display_array(self):
        print("Array:", self.array)
        print("Shape:", self.array.shape)
        print("Data Type:", self.array.dtype)
        print("Type:", type(self.array).__name__)
        print("Size:", self.array.size)
        print("Number of Dimensions:", self.array.ndim)
        print("Mean:", self.array.mean())
        print("Sum:", self.array.sum())
        print("Minimum Value:", self.array.min())
        print("Maximum Value:", self.array.max())
        print("Standard Deviation:", self.array.std())
        print("Variance:", self.array.var())

    def some_examples(self):
        print("Some Examples:")
        print("Array + 2:", self.array + 2)
        print("Array * 3:", self.array * 3)
        print("Array - 1:", self.array - 1)
        print("Array / 2:", self.array / 2)
        print("Array ** 2:", self.array ** 2)
        print("Array % 2:", self.array % 2)

        print("------------------------------------")
        print("ZEROEs EXAMPLES:")
        print("------------------------------------")
        print("zeros:", np.zeros(4))
        print("ones :", np.ones((2, 3)))
        print("range:", np.arange(0, 10, 2))     # start, stop, step
        print("lin  :", np.linspace(0, 1, 10))    # 10 evenly spaced points
        print("------------------------------------")
        print("RESHAPE EXAMPLES:")
        print("------------------------------------")
        m = np.arange(12).reshape(3, 4)
        print(m)
        print("shape:", m.shape)
        print("ndim :", m.ndim)
        print("size :", m.size)
        print("dtype:", m.dtype)

npd = Numpydemo(np.array([1, 2, 3, 4, 5]))
npd.display_array()
npd.some_examples()
'''
npd = Numpydemo(np.array([[1, 2, 3, 4, 5],[7, 9, 3, 0, 12]]))
npd.display_array()
npd.some_examples()
'''