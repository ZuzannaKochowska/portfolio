import pandas as pd
from sqlalchemy import create_engine

# Dane do logowania do bazy
user = "root"
password = "Farmazony10!"
host = "localhost"
port = "3306"
database = "companies_financial_rates"

# Utwórz silnik połączenia
engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}")

# Wczytaj plik CSV
df = pd.read_csv("all_companies_wide_with_ratios.csv")

# Zapisz dane do bazy MySQL
df.to_sql(name='companies_financial_rates', con=engine, if_exists='replace', index=False)

print("Plik CSV został zaimportowany do MySQL jako 'companies_financial_rates'")
