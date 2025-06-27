import csv
import pandas as pd

with open("../customer.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    data = []
    for row in reader:
        data.append(row)
headers = data[0]
rows = data[1:]

df = pd.DataFrame(rows, columns=headers)
df["Mobile Number"] = df["Mobile Number"].str.replace(r"\D", "", regex=True)
df = df[df["Mobile Number"].str.len() == 10]
df = df.copy()
df.index = range(len(df))

df.to_csv("../customer.csv", index=False)
