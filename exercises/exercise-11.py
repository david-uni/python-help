# 05/01/2021 exercise 11
import pandas as pd  # importing the pandas library with the alias 'pd'
import numpy as np
import matplotlib.pyplot as plt

# initialization
# in pandas in each dataframe all the values in each column must be of the same type
d = {'col1': [1, 2], 'col2': [3, 4]}
df1 = pd.DataFrame(d)  # creates a new dta frame from a dictionary

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
df2 = pd.DataFrame(a, columns=['col1', 'col2', 'col3'], index=[
                   'row1', 'row2', 'row3'])  # creates a new data frame from list

# properties
df2.columns  # returns all the columns names in the data frame
df2['col2']  # returns all the values in the given columns (of type Series)
df2.col2  # returns all the values in the given columns (of type Series)
# returns the type of each column in the dataframe (object stands for string)
df2.dtypes

# math operations
col_diff = df1['col2'] - df1['col1']  # math operations between two columns

# loc and iloc - names and indexes
df3 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=[
                   'a', 'b', 'c'], index=[3, 4, 5])
df3.iloc[:2]  # returns all the rows up to row at index 2 (not included)
df3.loc[:3]  # returns all the rows up to the row "named" 3 (included)

# csv files
file_name = 'countries-of-the-world.csv'
df = pd.read_csv(file_name)

# methods
df.head(3)  # returns the first 3 rows (default to 5 - df.head())
df.tail(3)  # returns the last 3 rows (default to 5 - df.tail())
df.sample(3)  # returns random 3 rows (default to 5 - df.sample())
df.info()  # return the info about the given dataframe (column names, number of non null values per column, memory usage)
df.describe()  # returns a description of the given dataframe
# returns a new dataframe and replace all the empty cells in the dataframe with the given value
df.fillna(0)
df.mean()  # return the average of the df
# replace all the empty cells in the column with the average of the column
df['Country'].fillna(df['Country'].mean(), inplace(True))
df = df.dropna()  # returns a new dataframe without the empty cells
# apply the given function on each cells
df['Area'] = df['Area'].apply(lambda x: x*2)
# runs all the df row by row (axis=1) and apply the given function on each raw
df.apply(lambda row: row * 2, axis=1)
new_row = {'col1': 1, 'col3': 5}
# returns a new df with the added row at the end (ignore_index recreate the indexes if True), missing columns will be filled with nan
df.append(new_row, ignore_index=True)
# returns a new df without the given colum (1 stands for axis=1 [axis=0 will drop the row])
df.drop('Area', 1)
len(df)  # returns the number of rows in the df
df['Area'].sum()  # returns the sum of the column

# masking
# returns a new df with only the cells that match the condition
df[df.Country != 'Iran']
# returns a new df with only the cells where Country value is "not" (~) one of ['Iran', 'Iraq']
df[~df.Country.isin(['Iran', 'Iraq'])]
df[df.Population > 1000 & (df.Region == 'ASIA')]  # combine multiple masks (&)

# joining (inner / outer)
df4 = pd.DataFrame({'User': [1, 2, 3, 4, 5, 6], 'Height': [
                   1.6, 1.8, 1.69, 2, 1.90, 1.84]})
df5 = pd.DataFrame({'User': [1, 3, 5], 'Weight': [60, 70, 80, 90, 55, 70]})
# megrge the 2 df into a new on by the column 'User'
pd.merge(pd4, pd5, on='User', how='inner')
# conplete here ###############################
pd.merge(pd4, pd5, on='User', how='outer')
# returns a new df with all the given dataframes concatenated by order
df6 = pd.concat([df4, df5])

# returns the name of the row with the max value
label_max = df.Population.idxmax()
# returns the value at row [label_max] and at column 'Country'
df.loc[label_max]['Country']

# data analysis
# returns a new df sorted by the given columns in ascending order
df.sort_values(['Population', 'Area'], ascending=True)
# grouping
# returns groups, each one contains a group-name (the shared value) and df
regions = df.groupby(['Region'])
for name, group in regions:
    label_max = group['Population'].idxmax()
    group.loc[label_max]['Country']
# chaining methods
# calculating the Population average per Region
df.groupby(['Region'])['Population'].mean()
# returns the maximal Deathrate average per Region
df.groupby('Region')['Deathrate'].mean().max()

# visualization
# creates an histogram of the given column data (bins - how much is each group)
ax = df.hist(column='GDP ($ per capita)', bins=10, grid=False, color='#86bf91')
ax.set_xlabel('GDP')  # set the label of the x axis
ax.set_ylabel('Count')  # set the label for the y axis
plt.show()  # uses plt to show the graph

# histogram of two columns (alpha set the opacity)
ax = df[['Birthrate', 'Deathrate']].plot.hist(bins=12, alpha=.5)
plt.show()

# creates a boxplot graph
boxplot = df.boxplot(columns=['Birthrate', 'Deathrate'])
plt.show()
