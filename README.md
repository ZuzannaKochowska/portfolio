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

BAZA DANYCH I **SQL**
Dodatkowo, przygotowano plik z zapytaniami SQL **profitability_analysis_queries.sql** , które można wykorzystać do analizy danych finansowych w relacyjnej bazie danych (MySQL).
Zakres zapytań obejmuje m.in.:
- tworzenie tabel i załadowanie danych,
- obliczanie rentowności (ROA, ROE, EBITDA Margin, Net Profit Margin),
- porównania między firmami,
- filtrowanie spółek o wysokiej/zbyt niskiej rentowności,
- sortowanie spółek według wskaźników finansowych.
