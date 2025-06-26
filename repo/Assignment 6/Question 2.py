import pandas as pd

df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['A', 'B', 'C']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Marks': [80, 72, 85]})
result = pd.merge(df1, df2, on='ID', how='inner')
print(result)

result = pd.merge(df1, df2, on='ID', how='left')
print(result)

result = pd.merge(df1, df2, on='ID', how='right')
print(result)

res = df1.join(df2,rsuffix="_right",lsuffix="_left")
print(res)

df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['A', 'B', 'C'],'dept':['HR','Sales','HR']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Marks': [80, 72, 85],'dept':['Sales','HR','IT']})
result = pd.merge(df1, df2, on=['ID', 'dept'], how='inner')
print(result)
