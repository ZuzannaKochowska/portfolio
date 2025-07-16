import pandas as pd

# Wczytaj dane
df = pd.read_csv("all_companies.csv")

rename_dict = {
    'Przychody ze sprzedaży': 'Revenue',
    'Zysk/strata ze sprzedaży': 'Gross_Profit',
    'Pozostałe przychody operacyjne': 'Other_Op_Income',
    'Zysk/strata z działalności operacyjnej': 'Operating_Profit',
    'Zysk/strata brutto': 'Profit_Before_Tax',
    'zysk/strata netto udziałowców jednostki dominującej': 'Net_Profit',
    'Amortyzacja (noty)': 'Depreciation',
    'AKTYWA': 'Assets',
    'Kapitał własny udziałowców podmiotu dominującego': 'Equity',
    'Kapitał podstawowy': 'Share_Capital',
    'Przepływy operacyjne': 'Cashflow_Operating',
    'Przepływy inwestycyjne': 'Cashflow_Investing',
    'Nabycie rzeczowych aktywów trwałych oraz wartości niematerialnych': 'Capex',
    'Przepływy finansowe': 'Cashflow_Financing',
    'Przepływy pieniężne netto': 'Cashflow_Net',
    'EBITDA': 'EBITDA',
    'Stopa zwrotu z kapitału własnego (ROE)': 'ROE_reported',
    'Stopa zwrotu z aktywów (ROA)': 'ROA_reported'
}
df['Finacial Rate'] = df['Finacial Rate'].map(rename_dict)
df = df.drop_duplicates(subset=['Company', 'Finacial Rate'], keep='first')
# Pivot — firmy jako wiersze, wskaźniki jako kolumny
df_wide = df.pivot(index='Company', columns='Finacial Rate', values='Amount in PLN')
df_wide.columns.name = None  # Usuwa nazwę poziomu kolumn
df_wide = df_wide.reset_index()  # Przywraca kolumnę "Company" jako zwykłą kolumnę


df_wide.to_csv('all_companies_wide.csv', index=False)
# Podgląd nowej tabeli
print(df_wide.head())
