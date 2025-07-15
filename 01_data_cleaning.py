import pandas as pd

column_names = ['Finacial Rate', 'Amount in PLN']

df = pd.read_csv('zabka.csv', header=None, names=column_names)
df['Amount in PLN'] = df['Amount in PLN'].str.replace(' ', '', regex=False).str.replace(',', '.', regex=False).astype(float)

df['Amount in PLN'] = df['Amount in PLN'].astype(float) * 1000
df['Company'] = 'Żabka'
df.to_csv("zabka_clean.csv", index=False)

