import pandas as pd

column_names = ['Finacial Rate', 'Amount in PLN']

df = pd.read_csv("../kghm.csv", header=None, names=column_names)
df['Amount in PLN'] = df['Amount in PLN'].str.replace(' ', '', regex=False).str.replace(',', '.', regex=False).astype(float)

percent_keywords = ['ROE', 'ROA', 'wskaźnik']
mask = ~df['Finacial Rate'].str.lower().str.contains('|'.join([k.lower() for k in percent_keywords]))
df.loc[mask, 'Amount in PLN'] = df.loc[mask, 'Amount in PLN'] * 1000
df['Company'] = 'KGHM'
df.to_csv("../kghm_clean.csv", index=False)


