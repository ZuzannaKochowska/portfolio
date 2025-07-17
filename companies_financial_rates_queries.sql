1. Firmy z największym zwrotem kapitału / Companies with the highest return on equity (ROE_) 
SELECT Company, ROE_reported, ROE 
FROM companies_financial_rates
ORDER BY ROE_reported DESC;

2. Firmy z najniższym wskaźnikiem zadłużenia / Companies with the lowest debt-to-equity ratio
SELECT Company, Debt_to_Equity
FROM companies_financial_rates
ORDER BY Debt_to_Equity ASC;

3. Firmy z najwyższą marżą EBITDA / Companies with the highest EBITDA margin
SELECT Company, EBITDA
FROM companies_financial_rates
ORDER BY EBITDA DESC;

4.Porównanie płynności bieżącej i szybkiej firm / Comparison of current and quick liquidity across companies
SELECT Company, Current_Ratio, Quick_Ratio
FROM companies_financial_rates
ORDER BY Current_Ratio DESC;

5.Firmy, które mają ujemny zysk netto / Companies with a negative net profit
SELECT Company, Net_Profit
FROM companies_financial_rates
WHERE Net_Profit < 0;

6.Średni ROA i ROE dla całej grupy firm / Average ROA and ROE for across all companies
SELECT ROUND(AVG(ROA_reported),2) AS avg_ROA_reported, 
		ROUND(AVG(ROA),2) AS avg_roa, 
        ROUND(AVG(ROE_reported),2) AS avg_ROE_reported, 
        ROUND(AVG(ROE),2) AS avg_roe
FROM companies_financial_rates;

7.Top 5 firm z najwyższym wskaźnikiem płynności bieżącej / Top 5 companies with the highest current ratio
SELECT Company, Current_Ratio
FROM companies_financial_rates
ORDER BY Current_Ratio DESC;

8.Firmy z najwyższą amortyzacją w PLN / Companies with the highest depreciation (PLN)
SELECT Company, Depreciation
FROM companies_financial_rates
ORDER BY Depreciation DESC;
