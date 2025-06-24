import pandas as pd
'''
a =[10, 20, 30, 40]
s = pd.Series(a,index=["x","y","z","a"])
data ={"day1": 421, "day2":233, "day3":453}
s = pd.Series(a,index=["x","y","z","a"])
s = pd.Series(data, dtype=float, index=["day1","day2"])
print(type(s.tolist()))
print(type(s))
data = {
    "num": [10,20,30],
    "alpha": ["a","b","c"]
}

df.index = [10, 20, 30]
'''
df = pd.DataFrame([["0", "o","x"],["10", "a","y"],["20", "b","z"],["30", "c","z"]],  columns=["Col1", "Col2","Col3"], index= [0,1,2,3])
df.iloc[0:2, 1:3] = [["l","w"],["m","x"]]
print(df[df["Col1"]=="0"])  

# print(pd.__version__)