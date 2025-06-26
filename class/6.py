import pandas as pd

data ={"A": [10, 20, 30, 40], "B": [1, 2.0, 3, 4], "C": [5, 6, 7, 8]}

df = pd.DataFrame(data, index=pd.to_datetime(["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04"]))

df1=df+32

df1 = df1.drop(columns=["C"], index=0)
# print(df)
# df["Add"]= df["A"] + df["B"] + df["C"]
print("Addition :\n", df + df1)
