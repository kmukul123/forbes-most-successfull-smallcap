

import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Expro Group Holdings":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Expro Group is a global oil and gas services company. It provides a range of services and products across the well lifecycle, including well construction, well flow management, and production services, for both offshore and onshore projects. [highlight]Expro Group Holdings' competitive moat is built on its technological expertise (87 active patents, proprietary designs), global presence, strong customer relationships, operational efficiency, and specialized market position in complex well construction and subsea well access. It focuses on high value-add, technology-enabled solutions.[/highlight] [neg]However, Morningstar assesses its economic moat as \"None.\"[/neg] [pos]Expro Group Holdings has a Return on Invested Capital (ROIC) of 5.63% (Finance Charts, as of June 2025), a significant improvement from its 3-year average of -0.84%. Its Return on Capital Employed (ROCE) is 7.16% (StockAnalysis).[/pos] [link to Expro Group Holdings Investor Relations](https://investors.expro.com/) [link to Finance Charts XPRO ROIC](https://financecharts.com/stocks/xpro/roic) [link to StockAnalysis XPRO ROIC/ROCE](https://stockanalysis.com/stocks/xpro/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Ownership is primarily held by institutional investors, many of whom were creditors prior to the company's restructuring and merger. Insider ownership is approximately 1.17% (TipRanks).[/pos] [link to TipRanks XPRO Ownership](https://www.tipranks.com/stocks/xpro/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company emerged from a merger with a healthier balance sheet but still manages debt related to its global operations and equipment fleet. [pos]As of March 2025, Expro Group Holdings reported $179.3 million in cash, with total debt of $121.1 million, resulting in a net cash position of $58.2 million. As of December 2024, cash was $185 million and debt was $121 million. There is no information about stock dilutions or buybacks.[/pos] [link to Expro Group Holdings Q1 2025 Earnings Release](https://investors.expro.com/news-releases/news-release-details/2025/Expro-Group-Holdings-N.V.-Announces-First-Quarter-2025-Results/default.aspx) [link to Moomoo XPRO Financials](https://www.moomoo.com/us/stock/XPRO/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Scalability is tied to the global oil and gas capital expenditure cycle. Growth comes from winning contracts for large-scale international projects, expanding its technology offerings (like well testing and subsea services), and capitalizing on energy transition trends."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Expro Group Holdings entry updated successfully.")
