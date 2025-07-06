
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Flexsteel Industries":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Flexsteel Industries is a manufacturer, importer, and marketer of residential and commercial upholstered and wood furniture products in the United States. It is known for its patented blue steel spring technology, which provides durability. [highlight]Flexsteel Industries' competitive moat is built on its patented Flexsteel Spring Unit (durability, comfort), strong brand reputation, extensive distribution network, vertical integration, diverse product portfolio, financial strength, operational efficiency, and continuous product innovation.[/highlight] [pos]Flexsteel Industries has a Return on Capital Employed (ROCE) of 12.07% and a Return on Invested Capital (ROIC) of 7.19% (StockAnalysis). Its ROIC is also reported as 9.64%, which is higher than its 3-year average of 4.50%.[/pos] [link to Flexsteel Industries Investor Relations](https://www.flexsteel.com/investors) [link to StockAnalysis FLXS ROIC/ROCE](https://stockanalysis.com/stocks/flxs/roic/) [link to Finance Charts FLXS ROIC](https://financecharts.com/stocks/flxs/roic)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership is moderate, with TipRanks reporting 15.52% and Stock Titan indicating 29.85%. The company has a history of long-tenured management. Insiders have both bought and sold shares recently.[/pos] [link to TipRanks FLXS Ownership](https://www.tipranks.com/stocks/flxs/ownership) [link to Stock Titan FLXS Ownership](https://stocktitan.net/news/FLXS/flexsteel-industries-inc-insider-trades-flxs-stock-titan-29-85-insider-ownership-as-of-july-1-2025.html)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company maintains a very strong balance sheet with little to no debt, providing significant financial flexibility through economic cycles. [pos]As of March 31, 2024, Flexsteel Industries reported a cash balance of $4.6 million. The company has reduced its debt, with repayments of $3.7 million for the quarter, and had approximately $46.9 million available under its secured line of credit. The company has a long history of uninterrupted dividend payouts (87 years).[/pos] [link to Flexsteel Industries Q3 2024 Earnings Release](https://www.flexsteel.com/news-releases/news-release-details/2024/Flexsteel-Industries-Inc.-Reports-Third-Quarter-Fiscal-2024-Financial-Results/default.aspx)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Moderately scalable. Growth is tied to the health of the housing and home furnishings market. Scalability comes from expanding its dealer network, growing its e-commerce presence, and optimizing its global supply chain."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Flexsteel Industries entry updated successfully.")
