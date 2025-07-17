import pandas as pd
import os
import glob

folder_path = './03_pivot_table.py'
df = pd.read_csv("all_companies_wide.csv")

df['ROA'] = df['Net_Profit'] / df['Assets'],
df['ROE'] = df['Net_Profit'] / df['Equity'],
df['ebitda'] = df['EBITDA'] / df['Revenue'],
df['Net_Profit_Margin'] = df['Net_Profit'] / df['Revenue'],
df['debt_to_equity'] = (df['Short_Term_Liabilities'] + df['Long_Term_Liabilities']) / df['Equity']
