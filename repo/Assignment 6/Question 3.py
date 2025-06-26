import pandas as pd

df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['A', 'B', 'C']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Marks': [80, 72, 85]})
res = pd.concat([df1, df2], ignore_index=True)

df3 = pd.DataFrame({'ID':[3,4,5],'Score':[50,30,10],'s_id':['s1','s2','s3']})
final_df = pd.merge(res, df3, on='ID', how='inner')
print(final_df)