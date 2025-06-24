import pandas as pd

list = [10, 20, 30]
df = pd.DataFrame(list, columns=["num"])
df.index = [10, 20, 30]
print("DataFrame from 2-D list:")
print(df)
print()

dict = {
    "num": [10, 20, 30],
    "alpha": ["a", "b", "c"]
}
df = pd.DataFrame(dict)
df.index = [10, 20, 30]
print("DataFrame from dictionary:")
print(df)
print()

lol=[[10, "a"], [20, "b"], [30, "c"]]
df = pd.DataFrame(lol, columns=["num", "alpha"])
df.index = [10, 20, 30]
print("DataFrame from list of lists:")
print(df)
print()

lot=[(10, "a"), (20, "b"), (30, "c")]
df = pd.DataFrame(lot, columns=["num", "alpha"])
df.index = [10, 20, 30]
print("DataFrame from list of tuples:") 
print(df)
print()

lod =[{"num": 10, "alpha": "a"}, {"num": 20, "alpha": "b"}, {"num": 30, "alpha": "c"}]
df = pd.DataFrame(lod)
df.index = [10, 20, 30]
print("DataFrame from list of dictionaries:")
print(df)