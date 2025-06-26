import pandas as pd
dates = ['2025-06-25', '2025-06-26', '2025-06-27']
date_series = pd.to_datetime(dates)
df = pd.DataFrame({'Value': [1,2, 3]}, index=date_series)
print(df)