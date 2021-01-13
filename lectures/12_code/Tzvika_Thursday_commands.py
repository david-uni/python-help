# coding: utf-8
import pandas as pdimport matplotlib.pyplot as plt

df = pd.read_csv("StudentsGrades.csv")
df.index
type(df.index)
df["Name"]
type(df["Name"])
df["Programming"]
df.Programming
df.info()
df.Programming
df.Programming*2
df*2
df.Art-df.History
df.drop('Name', 1)
df.drop('Name', axis=1)
df.drop(0)
df.drop(3)
df['x'] = range(13)
df.drop('x',1)
df=df.drop('x',1)
type(df)
df.mean()
df.mean(axis=1)
df.sum()
s = df.sum()
s
s['Name']
list(s)
df['Avg'] = df.mean(axis=1)
df.append(df)
df.append(df, ignore_index=True)
type(df.loc)
df.loc[0, :]
df.loc[0, 'Programming']
df.loc[3:6,]
df.loc[3:6, 'Math':]
df.iloc[3:6, 4:7]
df.loc[3:6, 'Math':]
df.loc[:, 'Math']
df.Avg < 70
df.Avg < 75
df.Avg > 75
df[df.Avg > 75]
df.loc[df.Avg > 75,:]
df.loc[2:'Programming']=60
df.loc[2:'Programming']
df = pd.read_csv("StudentsGrades.csv")
df['Avg'] = df.mean(axis=1)
df.loc[df.Programming < 60, "Programming"]
df.loc[df.Programming < 60, "Programming"] = 60
df.Programming < 60
#df < 60 # error
df_no_names = df.drop('Name', 1)
df_no_names = df_no_names.drop('Avg', 1)
df_no_names < 60
(df_no_names < 60).sum()
(df_no_names < 60).sum().sum()
(df_no_names < 60).sum(axis=1).sum()
(df_no_names < 60).sum(axis=1)
df_no_names < 60
df[df_no_names < 60]
df[df_no_names < 60].count()
df.loc[:,['Name','Avg']]
df.loc[:,['Name','Avg','Avg']]
df[['Name','Avg','Avg']]
df.Avg.max()
df.Avg.idxmax()
df.Avg
idxmax = df.Avg.idxmax()
df.loc[idxmax]
df.loc[idxmax, "Name"]
df.mean()
df.append(df.mean(), ignore_index=True)
df.mean()
df.mean().idxmax()
df.boxplot()
import matplotlib.pyplot as plt
df.boxplot()
plt.show()
