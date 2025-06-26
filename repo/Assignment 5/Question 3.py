import pandas as pd
d = {
    'A':['a','b','c'],
    'B':[4,9,18],
    'C':['c1','c2','c3']
}
df1 = pd.DataFrame(d)
for i in range(len(df1)):
    name = df1.iloc[i, 0]
    age = df1.iloc[i, 1]
    print(f"Name: {name}, Age: {age}")

df = df1[df1['B']>5]
print(df)

row = df1.iloc[1]
print(row)

select = df.iloc[:2][['A']]
print(select)

d = df1[df1['B']>5].index
drop_row = df1.drop(d)
print(drop_row)

new_row = pd.DataFrame({'A': ['d'], 'B': [26],'C':['c3']})

Df1 = df1.iloc[:2]
Df2 = df1.iloc[2:]

df = pd.concat([Df1, new_row, Df2], ignore_index=True)

print(df)

row_list = df1.values.tolist()
print(row_list)