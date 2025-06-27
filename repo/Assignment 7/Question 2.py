import pandas as pd
from datetime import datetime, timedelta

data = {
    "name": ["Mahendra", "Sachin", "Suresh"],
    "date_str": ["2024-06-01", "2024-06-02", "2024-06-03"],
}
df = pd.DataFrame(data)

df["date"] = pd.to_datetime(df["date_str"])

df["date_plus_7"] = df["date"] + timedelta(days=7)

df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day

print(df)
