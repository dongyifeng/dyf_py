import pandas as pd

df = pd.read_excel(io="/Users/dongyf/Desktop/1.xlsx", skiprows=[1], usecols="C:D")
df.columns = ["name", "level"]
df.groupby("name")["level"].value_counts().to_excel("/Users/dongyf/Desktop/2.xlsx")
