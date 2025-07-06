

import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Gorman-Rupp":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """The Gorman-Rupp Company designs, manufactures, and sells pumps and pump systems for use in water, wastewater, construction, industrial, and fire protection applications. It is known for its high-quality, durable products. [highlight]Gorman-Rupp's competitive moat is built on its engineering expertise and product innovation (12.3% annual innovation rate), ability to provide customized solutions, diverse end markets and geographic diversification (47 countries), strong customer service and aftermarket support, product reliability (99.7% uptime), and long operating history (since 1933). It is also a \"Dividend King\" with 52 consecutive years of dividend increases.[/highlight] [pos]Gorman-Rupp has a Return on Capital Employed (ROCE) of 11.94% and a Return on Invested Capital (ROIC) of 7.66% (StockAnalysis). Its ROIC was 5.4% in 2024, and its ROCE was 11.94%.[/pos] [link to Gorman-Rupp Investor Relations](https://www.gormanrupp.com/investor-relations/) [link to StockAnalysis GRC ROIC/ROCE](https://stockanalysis.com/stocks/grc/roic/) [link to SureDividend GRC Dividend History](https://www.suredividend.com/gorman-rupp-dividend/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]The founding family has a significant influence and ownership stake, promoting a culture of quality and long-term stability. Insider ownership varies across sources, from 0.50% (Trendlyne) to 21% (Simply Wall St).[/pos] [link to Trendlyne GRC Ownership](https://trendlyne.com/equity/share-holding/1400/GRC/latest/gorman-rupp-co/) [link to Simply Wall St GRC Ownership](https://simplywall.st/stocks/us/industrials/nyse-grc/the-gorman-rupp/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company has historically maintained a very conservative balance sheet with low debt, but recently took on debt to finance a major strategic acquisition. [pos]As of March 31, 2025, Gorman-Rupp reported $333.7 million in total debt, with a $14.6 million reduction in total debt during Q1 2025. Operating cash flow for Q1 2025 was $21.1 million. The company has a $50 million share repurchase program authorized in October 2021, with $49.0 million available as of December 2021. A 1.3:1 stock split occurred in December 2013.[/pos] [link to Gorman-Rupp Q1 2025 Earnings Release](https://www.gormanrupp.com/news-releases/news-release-details/2025/The-Gorman-Rupp-Company-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to Macrotrends GRC Stock Splits](https://www.macrotrends.net/stocks/charts/GRC/gorman-rupp/stock-splits)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Scalable through strategic acquisitions and by expanding into new geographic markets. Growth is driven by the need for water and wastewater infrastructure upgrades and by industrial capital spending."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Gorman-Rupp entry updated successfully.")
