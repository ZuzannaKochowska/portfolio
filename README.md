ENGLISH VERSION BELOW

**Analiza Rentowności Firm na Podstawie Danych Finansowych (Q1 2025)**

Projekt ma na celu ocenę rentowności wybranych spółek notowanych na GPW (indeks WIG20) na podstawie ich wyników finansowych za I kwartał 2025 roku. Analiza została przeprowadzona w języku **Python**, z wykorzystaniem bibliotek do analizy i wizualizacji danych oraz zapytań SQL.

Zakres analizy:

1. **Pozyskanie danych:**
   - Surowe dane finansowe spółek WIG20 pobrano ze strony [gpw.pl](https://www.gpw.pl).
   - Dane zapisano w plikach `.xlsx`, a następnie przekonwertowano do `.csv`.

2. **Czyszczenie i przekształcanie danych (ETL):**
   - Dane zostały załadowane i oczyszczone w języku Python (moduły `pandas`, `numpy`).
   - Ujednolicono nazwy kolumn, usunięto błędy oraz uzupełniono brakujące dane.
   - Dane zostały połączone w jedną tabelę z użyciem funkcji `pivot`.
     
3. **Import do relacyjnej bazy danych:**
   - Dane zaimportowano do **MySQL**.
   - W folderze `/sql` znajduje się plik `profitability_analysis_queries.sql` zawierający zapytania SQL do analizy finansowej.

4. **Analiza danych i wizualizacje:**
   - Przeprowadzono analizę eksploracyjną w **Jupyter Notebook**.
   - Wykorzystano biblioteki:
     - `pandas` (analiza danych),
     - `matplotlib`, `seaborn` (wizualizacje),
     - `scikit-learn` (klasteryzacja, PCA).
   
# Obliczone wskaźniki finansowe

Dla każdej spółki wyliczono:

| Wskaźnik                    | Opis                                           | Jednostka    |
|-----------------------------|------------------------------------------------|--------------|
| **ROE** (Return on Equity) | Rentowność kapitału własnego                   | %             |
| **ROA** (Return on Assets) | Rentowność aktywów                             | %             |
| **Net Profit Margin**      | Marża zysku netto                              | %             |
| **EBITDA Margin**          | Marża EBITDA                                   | %             |
| **Debt to Equity**         | Wskaźnik zadłużenia do kapitału własnego       |razy (x)       |

 Dane kwartalne (Q1 2025):  
- **Zysk netto, EBITDA i przychody** – dane z I kwartału 2025.  
- **Aktywa i kapitał własny** – dane bilansowe na dzień **31.03.2025**. 

Struktura repozytorium:
📁 data/ -> dane źródłowe (CSV)
📁 report/ -> raport analizy w pdf
📁 notebooks/ -> analizy i wykresy w Jupyter Notebook
📁 sql/ -> zapytania SQL (MySQL)
📁 scripts/ -> skrypty do czyszczenia, pivotowania, importu
README.md -> opis projektu

UWAGA
Ten projekt służy wyłącznie celom edukacyjnym i nie stanowi porady inwestycyjnej.
Wskaźniki finansowe są oparte na kwartalnych wynikach i mogą różnić się od oficjalnych, zannualizowanych danych publikowanych przez GPW lub instytucje finansowe.

---------------------------------------------------

**Profitability Analysis of Companies Based on Financial Data (Q1 2025)**

This project aims to assess the profitability of selected companies listed on the Warsaw Stock Exchange (WSE), specifically those included in the WIG20 index, based on their financial performance for the first quarter of 2025. The analysis was conducted in **Python**, using libraries for data processing and visualization, as well as SQL queries.

---

Scope of Analysis:

1. **Data Acquisition:**
   - Raw financial data for WIG20 companies was sourced from [gpw.pl](https://www.gpw.pl).
   - The data was initially saved as `.xlsx` files and then converted to `.csv`.

2. **Data Cleaning and Transformation (ETL):**
   - The data was loaded and cleaned using Python (`pandas`, `numpy`).
   - Column names were standardized, errors were removed, and missing values were filled in.
   - The datasets were merged into a single pivot table using `pivot`.

3. **Importing into a Relational Database:**
   - The cleaned data was imported into a **MySQL** database.
   - SQL queries used for financial analysis are provided in the `/sql` folder (`profitability_analysis_queries.sql`).

4. **Data Analysis and Visualization:**
   - Exploratory analysis was performed in **Jupyter Notebook**.
   - Libraries used:
     - `pandas` for data analysis,
     - `matplotlib`, `seaborn` for visualizations,
     - `scikit-learn` for clustering and PCA.

---

Calculated Financial Ratios:

The following key financial indicators were calculated for each company:

| Metric                      | Description                                      | Unit       |
|----------------------------|--------------------------------------------------|------------|
| **ROE** (Return on Equity) | Profitability of shareholders' equity            | %          |
| **ROA** (Return on Assets) | Profitability of total assets                    | %          |
| **Net Profit Margin**      | Net income margin                                | %          |
| **EBITDA Margin**          | Earnings before interest, taxes, depreciation and amortization | % |
| **Debt to Equity**         | Leverage ratio (debt-to-equity)                 | times (x)  |

 **Quarterly data (Q1 2025):**  
- **Net profit, EBITDA, and revenue** are based on Q1 2025 financials.  
- **Assets and equity** are based on the balance sheet as of **March 31, 2025**.

---

Repository Structure:

📁 data/ → source data (CSV files)
📁 report/ → final analysis report (PDF)
📁 notebooks/ → Jupyter Notebook files with analysis and visualizations
📁 sql/ → SQL queries (MySQL)
📁 scripts/ → Python scripts for cleaning, pivoting, and importing data
README.md → project description

Notes:

- This project is for educational purposes only and does not constitute investment advice.
- The financial ratios are based on **quarterly** results and may differ from official, annualized figures published by WSE or financial services.

