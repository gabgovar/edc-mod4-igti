import pandas as pd

url = 'https://d17h27t6h515a5.cloudfront.net/topher/2017/October/59e4fe3d_titanic-data-6/titanic-data-6.csv'

df = pd.read_csv(url)

df["novacouna"] = df["Age"].apply(lambda x: x*2)

print(df.columns)

print(df.head())

print(df.shape)