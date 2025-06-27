import pandas as pd
import numpy as np
import re


# np.nan to Return NaN values in the DataFrame
# df.fillna(str) for filling NaN values with a specified value

# ffill(limit=int) for forward filling NaN values
# bfill(limit=int) for backward filling NaN values
df = pd.DataFrame(
    {"one": [1, 2, "3 d"], "two": [4, 5, 6], "three": [7, 8, 9]}, index="a b c".split()
)
df = df.replace({1: 100, 2: 200, 3: 300})
print(df)

df["one"] = df["one"].str.replace(r"\D+", "", regex=True).astype("int")

print(df["one"])
