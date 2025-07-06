

import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Ouster":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Ouster is a leading provider of high-resolution digital lidar sensors for the industrial automation, smart infrastructure, robotics, and automotive industries. Its digital lidar technology offers a combination of performance, reliability, and affordability. [highlight]Ouster's competitive moat is built on its technological leadership in digital lidar, a \"defense moat\" through Blue UAS Framework approval, a software-driven \"Physical AI\" strategy, market diversification beyond automotive, cost efficiency, strategic partnerships, improving gross margins, and a strong financial position.[/highlight] [pos]Ouster has a Return on Invested Capital (ROIC) of -30.23% and a Return on Capital Employed (ROCE) of -55.65% (StockAnalysis).[/pos] [link to Ouster Investor Relations](https://investors.ouster.com/) [link to StockAnalysis OUST ROIC/ROCE](https://stockanalysis.com/stocks/oust/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Founders and executives hold a stake in the company, alongside significant ownership by venture capital and institutional investors. Insider ownership varies across sources, from 6.61% (TipRanks) to 32.11% (WallStreetZen). Krishna Kantheti is the largest individual shareholder (4.54%). Insiders have both bought and sold shares in the last 24 months.[/pos] [link to WallStreetZen OUST Ownership](https://www.wallstreetzen.com/stocks/us/semiconductors/nyse-oust/ouster/ownership) [link to TipRanks OUST Ownership](https://www.tipranks.com/stocks/oust/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """Has utilized debt and equity financing to fund its R&D and scale its manufacturing operations to meet growing demand for lidar sensors. [pos]As of March 2025, Ouster's cash, cash equivalents, and marketable securities were approximately $168.19 million. Total debt was approximately $18.97 million, resulting in a net cash position of $149.23 million. The company repaid all outstanding balances under its revolving credit line in Q3 2024, and Macrotrends reports $0 long-term debt in 2024.[/pos] [link to Ouster Q1 2025 Earnings Release](https://investors.ouster.com/news-releases/news-release-details/2025/Ouster-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to GuruFocus OUST Financials](https://www.gurufocus.com/term/cash_to_debt/NYSE:OUST)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Very high scalability. As the cost of lidar decreases, its applications expand exponentially. Growth is driven by increasing adoption in diverse markets. The company scales by reducing manufacturing costs and securing large-volume production deals."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Ouster entry updated successfully.")
