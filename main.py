import pandas as pd
csv_path = '1.csv'
df = pd.read_csv(csv_path)

c = df.loc[0, "Album"]

print(c)