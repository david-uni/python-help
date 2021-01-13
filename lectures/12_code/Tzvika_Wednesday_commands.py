# coding: utf-8
import pandas as pdimport matplotlib.pyplot as plt

df = pd.read_csv("StudentsGrades.csv")
df.columns
df.index
type(df.index)
df['Name']
type(df['Name'])
names = df['Name']
names[0]
names[5]
#df[0]  # error
df['Programming']
df.Programming
df.dtypes
type(df.dtypes)
df.dtypes.Name
df.dtypes.Programming
df.info()
df.History
df.History*2
df.Art-df.History
a=df.Art-df.History
a.to_numpy()
list(a)
pd.read_csv("StudentsGrades.csv", index_col=0)
df.Art-df.History
df.History*2
df.History = df.History*2
df.History = df.History//2
#df.drop('Name')  # error
df.drop('Name', axis=1)
df['x'] = range(13)
df.drop('x',1,inplace=True)
df.mean()
df.mean(axis=1)
df.mean(axis=1, numeric_only=True)
df.mean(axis=1)
df['Avg'] = df.mean(axis=1)
df.max()
df.max(axis=1)
df.append(df)
df.append(df)
df.drop(0)
df.Avg < 75
df.Avg > 75
df[df.Avg > 75]
b = df[df.Avg > 75]
b.reindex()
b.reindex(axis=0)
b.reindex(axis=1)
b.index = range(len(b))
df.loc[1,'Programming']
df.iloc[0,0]
df.iloc[0,5]
df.iloc[0:3,5:7]
df.loc[3:,'Math':]
df.loc[:,'Math']
df["Programming"] < 60
df.loc[df["Programming"] < 60]
df.loc[df["Programming"] < 60, "Programming"]
df.loc[df["Programming"] < 60, "Programming"] = 60
df.loc[df["Programming"] < 60, "Name"]
df.loc[df["Programming"] < 70, "Name"]
df.loc[df["Programming"] < 70, ["Name", "Math"]]
df.loc[df["Programming"] < 70, ("Name", "Math")]
#df < 60  # error
df_no_names = df.drop('Name', 1)
df_no_names < 60
(df_no_names < 60).sum()
(df_no_names < 60).sum().sum()
(df_no_names < 60).count()
(df_no_names < 60)
df_no_names[df_no_names < 60]
(df_no_names < 60)
(df_no_names < 60).sum(axis=1)
df.max()
df.Avg.max()
df.Avg.idxmax()
max_idx = df.Avg.idxmax()
df.loc[max_idx]
df.loc[max_idx].Name
df.mean()
df.append(df.mean(), ignore_index=True)
df.boxplot()
plt.show()
df['Programming'] < 60
df['Stellar Cartography'] < 60
(df['Programming'] < 60) | (df['Stellar Cartography'] < 60)
(df['Programming'] < 60) & (df['Stellar Cartography'] < 60)