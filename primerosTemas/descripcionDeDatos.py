import pandas as pd
df=pd.read_csv('tratamientoFrijoles.csv')
g = df.groupby('Fertilizante')
print(df)
print(g.describe())

