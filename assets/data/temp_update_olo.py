
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "OLO":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Olo is a leading B2B SaaS company that provides a platform for restaurants to manage their digital ordering, delivery, and payment operations. Its modules include ordering, dispatch (for delivery), and rails (for integrating with third-party marketplaces. [pos]OLO has a Return on Invested Capital (ROIC) of -2.03% and a Return on Capital Employed (ROCE) of -3.15% (StockAnalysis).[/pos] [link to Olo Investor Relations](https://investors.olo.com/) [link to StockAnalysis OLO ROIC/ROCE](https://stockanalysis.com/stocks/olo/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]The founder and CEO holds a significant ownership stake and voting control, ensuring a product-focused and long-term strategic direction. Insider ownership varies across sources, from 5.16% (Simply Wall St) to 39.33% (MarketBeat).[/pos] [link to Simply Wall St OLO Ownership](https://simplywall.st/stocks/us/software/nyse-olo/olo/ownership) [link to MarketBeat OLO Ownership](https://www.marketbeat.com/stocks/NYSE/OLO/institutional-ownership/)"""

        # Update balancesheet with cash levels and debt details
        company["DESCRIPTION"]["balancesheet"] = """The company is debt-free and has a very strong cash position from its IPO and subsequent operations, which it uses to invest in R&D. [pos]As of March 31, 2025, OLO reported $40.1 million in cash and cash equivalents, with no long-term debt. The company has a history of share repurchases, with $10.0 million authorized for buybacks in 2024.[/pos] [link to Olo Q1 2025 Earnings Release](https://investors.olo.com/news-releases/news-release-details/2025/Olo-Announces-First-Quarter-2025-Financial-Results/default.aspx)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Highly scalable SaaS model. Growth is driven by adding more restaurant locations to its platform and by upselling additional modules (like payments) to its existing customer base. The ongoing digitization of the restaurant industry provides a long runway for growth."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("OLO entry updated successfully.")
