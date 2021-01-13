# 10/01/2021 Lesson 12

import pandas as pd  # import the library and set an alias
import numpy as np  # import the library and set an alias
import matplotlib.pyplot as plt

df = pd.DataFrame({'a': [1, 2], 'b': [3, 4], 'c': [5, 6]}, index=['aa', 'bb'])

df.values  # returns the values of the df as a numpy array
df['a'].values  # returns the values of the column as a numpy array

# returns a new transposed df (also transpose the columns and rows names)
df1 = df.T

df2 = df1.sum()  # returns a new df with the sums of the columns (can be set to sum rows using axis=1)
id_max = df2.idxmax()  # returns the row name of the max value
id_min = df2.idxmin()  # returns the row name of the min value

# returns a new df containing the given df concatented by columns - vertical stacking (can be changed to rows [horizontal stacking] with axis=1)
df3 = pd.concat([df, df], axis=1)


# plotting
# simple graph
x = np.arange(1, 6)
y = np.array([50, 20, 30, 90, 100])
plt.plot(x, y)  # set the graph
plt.show()  # shows the graph in a graphic interface

x = a.arange(1, 6)
y1 = np.array([50, 20, 30, 90, 100])
y1 = np.array([60, 10, 80, 30, 100])
plt.plot(x, y1-y2, marker='o')  # a graph of the diffs with dots at each x

# numpy matrices
np.dot()  # matrix multiplication by the math rules
# returns a new numpy array containing only unique values
arr2 = np.unique(arr1)

# set (like a list of unique values)
my_set1 = set()  # creates a new empty set
my_set2 = {1, 3, 2}  # creates anew set with initial values
lst = [1, 2, 3, 2, 1, 1, ]
my_set3 = set(lst)  # creates a set from the lst values
# returns a new set containing only the values that exist in both sets
my_set1.intersection(my_set2)
# returns a new set containing the values from both sets
my_set1.union(my_set2)
