# 03/01/2021 Lesson 11

import pandas as pd  # import the library and set an alias
import numpy as np  # import the library and set an alias

# df = pd.read_csv('file_path') # import data from csv file as a numpy array
dict_data = {'column1': [1, 2, 3], 'column2': [4, 5, 6]}
df = pd.DataFrame(data=dict_data)
"""
df = [
    ['', 'column1', 'column2'],
    [0, 1, 4],
    [1, 2, 5],
    [2, 3, 6],
]
"""
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6]]), columns=[
                  'col1', 'col2', 'col3'], index=['aa', 'bb'])  # columns - columns names, index - rows names
x = df.loc['aa', 'col2']  # slice by row and column
x = df.iloc[0, 1]  # slice by indexes
y = df.iloc[0]  # slice by indexes - all row at index 0

for col in df.columns:
    pass

df['col1']  # returns the column by column name
len(df)  # return the number of rows in the data frame
df.dtypes  # return the type of each column in the data frame
df.info()  # provides the essential details about the data frame

# substract to data frames of the same size (built on numpy)
a = df['col1'] - df['col2']
# appends a new column at the end with the result
df['new_col'] = df['col1'] - df['col2']
df.new_col  # returns the column

new_df = df.drop('col1', axis=1)


def get_avg(row):
    return row.drop('col_name').mean()  # return the average


df.apply(get_avg, axis=1)  # apply the given function per row / column
df['Avg'] = df.mean(axis=1, numeric_only=True)

df.append(new_df, ignore_index=True)

df2 = df[df['col1'] > 1]  # masking

# count all the cells matching the condition per column, and than sum all
df[df > 2].count().sum()

# iterate with the row index and value
for index, row in df.itterrows():
    pass

df.Avg.idxmax()  # returns the index of the max value

pd.concat([df, df2])
# merge  by cowlumn-'col1' and only values that exist in both dfs
pd.concat(df, df2, on='col1', how='inner')
# merge  by cowlumn-'col1' and all values that exist at least in one df
pd.concat(df, df2, on='col1', how='outer')

# grouping
groups = df.groupby(['col1'])
for name, group in groups:
    pass

groups['Name'].max()

df3 = pd.DataFrame({'Name': ['David', 'Ella', 'Galia', 'Shir', 'Liell'], 'Programming': [
                   90, 89, 56, 77, 99], 'Biology': [78, 76, 23, 65, 99], 'Class': [1, 2, 1, 2, 3]})
