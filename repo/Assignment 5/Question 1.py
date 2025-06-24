import pandas as pd

dict = {
    "num": [10, 20, 30],
}

s = pd.Series(dict["num"])
print(s)

list = [10, 20, 30]
s = pd.Series(list)
print(s)

ind =int(input("Enter index to Access: "))
print(s[ind])