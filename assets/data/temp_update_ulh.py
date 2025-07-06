import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Universal Logistics Holdings":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Universal Logistics Holdings provides a comprehensive suite of transportation and logistics solutions across the U.S., Mexico, Canada, and Colombia. Services include trucking, intermodal, logistics, and value-added services. [highlight]Universal Logistics Holdings' competitive moat is built on its comprehensive suite of transportation and logistics solutions, significant insider ownership ensuring long-term focus, and its ability to leverage a network of agents and owner-operators for scalable growth.[/highlight] [pos]Universal Logistics Holdings has a Return on Capital Employed (ROCE) of 10.88% and a Return on Invested Capital (ROIC) of 7.78% (StockAnalysis). Its ROCE has remained stable at 11% over the last five years.[/pos] [link to Universal Logistics Holdings Investor Relations](https://www.universallogistics.com/investors/) [link to StockAnalysis ULH ROIC/ROCE](https://stockanalysis.com/stocks/ulh/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]The company is majority-controlled by its founding family, ensuring a long-term, strategic focus on the business. Insider ownership is significant, with approximately 74.57% (TipRanks) of the stock held by insiders. Matthew T. Moroun, the largest individual shareholder, owns 74.00% of the company.[/pos] [link to TipRanks ULH Ownership](https://www.tipranks.com/stocks/ulh/ownership) [link to WallStreetZen ULH Ownership](https://www.wallstreetzen.com/stocks/us/industrials/nasdaq-ulh/universal-logistics-holdings/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """Manages a moderate level of debt to finance its fleet of trucks, terminals, and strategic acquisitions, while maintaining financial flexibility. [pos]As of March 29, 2025, Universal Logistics Holdings reported cash and cash equivalents totaling $20.6 million, with outstanding debt at $740.0 million. The company conducted a modified \"Dutch auction\" tender offer in June 2022, repurchasing 164,189 shares for $4.6 million. Shareholders have not been significantly diluted in the past year.[/pos] [link to Universal Logistics Holdings Q1 2025 Earnings Release](https://www.universallogistics.com/news-releases/news-release-details/2025/Universal-Logistics-Holdings-Inc.-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to Simply Wall St ULH Financials](https://simplywall.st/stocks/us/industrials/nasdaq-ulh/universal-logistics-holdings/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Scalable through a mix of organic growth and acquisitions in the fragmented logistics industry. It can scale by adding more agents and owner-operators to its network, expanding its value-added services, and capitalizing on cross-border trade."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Universal Logistics Holdings entry updated successfully.")
