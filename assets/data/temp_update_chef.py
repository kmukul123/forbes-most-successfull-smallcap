
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Chefs' Warehouse":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """The Chefs' Warehouse is a premier distributor of specialty food products to the foodservice industry in North America. It supplies high-quality ingredients to independent restaurants, fine dining establishments, hotels, and specialty food stores. [highlight]Its competitive moat is built on its niche market focus (high-end culinary), curated product portfolio (exclusive and hard-to-find items), strong supplier relationships, exceptional customer service, and specialized distribution network.[/highlight] [pos]The Return on Capital Employed (ROCE) for The Chefs' Warehouse is 9.39%. Its Return on Invested Capital (ROIC) is 5.95% (StockAnalysis) or 6.89% (GuruFocus, TTM as of June 2025).[/pos] [link to Chefs' Warehouse Investor Relations](https://investors.chefswarehouse.com/) [link to StockAnalysis CHEF ROIC/ROCE](https://stockanalysis.com/stocks/chef/roic/) [link to GuruFocus CHEF ROIC](https://www.gurufocus.com/term/roic/NASDAQ:CHEF)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]The company's founders and executive team hold a meaningful stake, ensuring their interests are aligned with the company's performance. Insider ownership is approximately 10.08% (TipRanks) to 17.19% (WallStreetZen), with CEO Christopher Pappas holding 6.84% and COO John Pappas holding 3.82%.[/pos] [neg]However, in the last 24 months, insiders have sold more shares than they have purchased.[/neg] [link to TipRanks CHEF Ownership](https://www.tipranks.com/stocks/chef/ownership) [link to WallStreetZen CHEF Ownership](https://www.wallstreetzen.com/stocks/us/consumer-defensive/nasdaq-chef/the-chefs-warehouse/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company utilizes a significant amount of debt to finance its acquisitions and working capital needs, which is typical for a distribution business. [neg]As of March 31, 2025, total debt was $633.8 million, with a net debt of approximately $517.2 million.[/neg] [pos]Cash reserves were $116.5 million as of March 31, 2025.[/pos] [pos]The Chefs' Warehouse has a history of share buybacks, with $11.41 million repurchased as of March 31, 2025, and a new buyback plan authorized in November 2023.[/pos] [neg]However, the company has experienced significant stock dilution, with shares outstanding increasing from ~25.92 million in 2017 to almost 38 million, largely due to stock-based compensation. Preliminary guidance for fiscal year 2025 forecasts a diluted share count between 46.3 and 47.0 million shares, including potential conversion of senior convertible notes.[/neg] [link to Moomoo CHEF Financials](https://www.moomoo.com/us/stock/CHEF/financials) [link to TipRanks CHEF Buybacks](https://www.tipranks.com/stocks/chef/buybacks) [link to Chefs' Warehouse Q1 2025 Earnings Release](https://investors.chefswarehouse.com/news-releases/news-release-details/2025/The-Chefs-Warehouse-Reports-First-Quarter-2025-Results/default.aspx)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Highly scalable through a combination of organic growth (cross-selling to existing customers) and a proven strategy of acquiring smaller, regional specialty distributors. The fragmented nature of the market provides ample acquisition targets."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Chefs' Warehouse entry updated successfully.")
