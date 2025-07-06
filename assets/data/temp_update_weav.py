
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Weave Communications":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Weave Communications provides an all-in-one customer communication and engagement software platform for small and medium-sized businesses, primarily in the healthcare sector (dental, optometry, medical). It integrates phone, text, email, and payment systems. [highlight]Weave Communications' competitive moat is built on its proprietary all-in-one communication technology (integrating various functionalities), specialization in SMB healthcare, user-friendly interface, strong customer support, AI-powered innovations (Call Intelligence), and integrated payments platform (Weave Payments).[/highlight] [pos]Weave Communications has a Return on Capital Employed (ROCE) of -28.46% and a Return on Invested Capital (ROIC) of -15.71% (StockAnalysis).[/pos] [link to Weave Communications Investor Relations](https://investors.getweave.com/) [link to StockAnalysis WEAV ROIC/ROCE](https://stockanalysis.com/stocks/weav/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Backed by venture capital and institutional investors. Insider ownership varies across sources, from 28.80% (MarketBeat) to 73.50% (WallStreetZen).[/pos] [link to MarketBeat WEAV Ownership](https://www.marketbeat.com/stocks/NYSE/WEAV/institutional-ownership/) [link to WallStreetZen WEAV Ownership](https://www.wallstreetzen.com/stocks/us/software/nyse-weav/weave-communications/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """Maintains a strong balance sheet with a healthy cash position and no significant debt. [pos]As of March 31, 2025, Weave Communications reported $53.41 million in cash and cash equivalents. Total liabilities stood at $119.73 million. Net cash provided by operating activities was $14.1 million in 2024. There is no information about stock dilutions or buybacks.[/pos] [link to Weave Communications Q1 2025 Earnings Release](https://investors.getweave.com/news-releases/news-release-details/2025/Weave-Communications-Inc.-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to Simply Wall St WEAV Financials](https://simplywall.st/stocks/us/software/nyse-weav/weave-communications/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Highly scalable SaaS platform. Growth is driven by adding more business locations to its platform and by increasing the adoption of its integrated payments solution. It can also scale by expanding into new small business verticals beyond healthcare."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Weave Communications entry updated successfully.")
