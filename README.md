ENGLISH VERSION BELOW

**Analiza Rentowności Firm na Podstawie Danych Finansowych (Q1 2025)**

Projekt ma na celu ocenę rentowności wybranych spółek notowanych na GPW na podstawie ich wyników finansowych za I kwartał 2025 roku. 
Analiza została wykonana w języku Python i obejmuje obliczenie kluczowych wskaźników finansowych dla każdej firmy.

Zakres analizy:

Dla każdej spółki wyliczono:
- **ROA (Return on Assets)** - rentowność aktywów
- **ROE (Return on Equity)** - rentowność kapitału własnego
- **EBITDA Margin** - marża EBITDA
- **Net Profit Margin** - marża zysku netto
- **Debt to Equity Ratio** - wskaźnik zadłużenia do kapitału własnego

Wszystkie wskaźniki zostały obliczone na podstawie danych kwartalnych (Q1 2025) pobranych z gpw.pl, dlatego mogą różnić się od wartości publikowanych przez GPW, które zwykle oparte są na danych rocznych lub zannualizowanych.
**Uwaga**: Zysk netto, EBITDA oraz przychody są danymi za I kwartał 2025. Aktywa i kapitał własny pochodzą ze stanu na dzień 31 marca 2025.

Technologie:
- Python (pandas, matplotlib, seaborn)
- Jupyter Notebook
- Źródła danych: GPW, raporty finansowe spółek

BAZA DANYCH I SQL:

Dodatkowo, przygotowano plik z zapytaniami SQL **profitability_analysis_queries.sql** , które można wykorzystać do analizy danych finansowych w relacyjnej bazie danych (MySQL).
Zakres zapytań obejmuje m.in.:
- tworzenie tabel i załadowanie danych,
- obliczanie rentowności (ROA, ROE, EBITDA Margin, Net Profit Margin),
- porównania między firmami,
- filtrowanie spółek o wysokiej/zbyt niskiej rentowności,
- sortowanie spółek według wskaźników finansowych.

---------------------------------------------------

**Profitability Analysis of Companies Based on Financial Data (Q1 2025)**

This project aims to assess the profitability of selected companies listed on the Warsaw Stock Exchange (GPW) based on their financial results for Q1 2025. The analysis was conducted in Python and includes the calculation of key financial ratios for each company.

Scope of Analysis:

- For each company, the following indicators were calculated:
- ROA (Return on Assets) – profitability of assets
- ROE (Return on Equity) – profitability of equity
- EBITDA Margin – EBITDA profitability
- Net Profit Margin – net income margin
- Debt to Equity Ratio – ratio of total liabilities to equity

All ratios were calculated using quarterly data (Q1 2025) obtained from gpw.pl. Therefore, the values may differ from those published by GPW, which are usually based on annual or annualized data. Note: Net profit, EBITDA, and revenue reflect Q1 2025 performance. Assets and equity values are based on the balance sheet as of March 31, 2025.

Technologies Used:

- Python (pandas, matplotlib, seaborn)
- Jupyter Notebook
- Data sources: GPW, companies' financial reports

SQL Integration:
In addition, a SQL script file profitability_analysis_queries.sql is provided to support financial analysis in a relational database environment (MySQL). The SQL queries include:

- Creating tables and importing data
- Calculating profitability ratios (ROA, ROE, EBITDA Margin, Net Profit Margin)
- Comparing companies
- Filtering by high/low profitability
- Sorting companies by financial indicators
