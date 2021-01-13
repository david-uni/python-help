# 27/12/2020 Lesson 10

import numpy as np  # import the library and set an alias

a = np.array([0, 1, 2])  # initialize an array with numpy with 1 dimension
# initialize an array with numpy with 2 dimension
b = np.array([[0, 1, 2], [3, 4, 5]])

b.ndim  # get number of dimensions
b.shape
len(b)

# initialize an array with 1 dimension and the length of 5 and all the values all 0. as float by default
c = np.zeros(5, dtype=float)
# initialize an array with 3 dimension and all the values all 0 as int
d = np.zeros((2, 3, 2), dtype=int)

e = np.ones(5, dtype=float)  # the same as zeroes but with 1

f = np.arange(10)  # creates an array with the range 0 - 10 (without 10)
# creates an array with the range 1 - 10 (without 10), with jumps of 3
g = np.arange(1, 10, 3, dtype=float)

g[3:1:-1]  # slicing one dimensional array

# creates an array with 9 values between 1 and 5 with equals spaces
h = np.linspace(1, 5, 9)
i = np.random.random(5)  # creates an array with 5 random numbers
# creates an array with 5 random integers between 0 and 10
i = np.random.randint(0, 10, 5)

# reshape the 1 dimension array into a 2 dimension of 5x2
j = np.arange(10).reshape(5, 2)
x = j[2, 1]  # value at row 2 column 1
k = j[:2, :]  # get first 2 rows, and for each row get all the columns

l = np.arange(9).reshape(3, 3) + 5  # adds 5 to all the values in the matrix
# return a matrix containing boolean values, by the condition (only even numbers)
mask = np.arange(9, dtype=int).reshape(3, 3) % 2 == 0
# return a matrix containing only the values matching True in the mask
m = np.arange(9, dtype=int).reshape(3, 3)[mask]

# returns an array with boolean values, TRUE at indexes with matching values
comp = np.random.randint(0, 10, 15) == np.random.randint(0, 10, 15)
comp.any()  # returns True if at least one value is True, returns False otherwise
comp.all()
comp.nonzeros()
comp.sum()
comp.sum(axis=0)  # sum by columns (top to bottom)
comp.sum(axis=1)  # sum by rows (left to right)
comp.mean(axis=1)  # average by rows

# we can specify multiple rows by indexes, and even have duplicates
m[[0, 2, 1, 1, 0], :]

np.sort(np.arange(3).reshape(3, 3), axis=0)  # returns a sorted array by axis
np.arange(3).reshape(3, 3).sort(axis=0)  # sort the array itself by axis

# image processing
