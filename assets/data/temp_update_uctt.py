
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Ultra Clean Holdings":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Ultra Clean Holdings is a leading developer and supplier of critical subsystems and components for the semiconductor capital equipment industry. It provides gas delivery systems, weldments, and other high-purity components used in semiconductor manufacturing tools. [highlight]Ultra Clean Holdings' competitive moat is built on its integrated solutions and technological expertise, critical supplier status in the semiconductor supply chain, continuous innovation, global manufacturing footprint, and vertical integration strategy. Its services are essential for clients, suggesting high switching costs.[/highlight] [neg]However, it faces industry volatility, intense competition, and customer concentration risks.[/neg] [pos]Ultra Clean Holdings has a Return on Capital Employed (ROCE) of 5.56% and a Return on Invested Capital (ROIC) of 3.52% (StockAnalysis). Its ROIC was 3.55% (TTM as of July 2025). GuruFocus notes its ROIC (3.55%) does not match its WACC (11.45%), suggesting potential value destruction as it grows.[/pos] [link to Ultra Clean Holdings Investor Relations](https://ir.uct.com/) [link to StockAnalysis UCTT ROIC/ROCE](https://stockanalysis.com/stocks/uctt/roic/) [link to GuruFocus UCTT ROIC](https://www.gurufocus.com/term/roic/NASDAQ:UCTT)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership is modest, with Stock Titan reporting 2.1% and TipRanks reporting 2.68%.[/pos] [link to Stock Titan UCTT Ownership](https://stocktitan.net/news/UCTT/ultra-clean-holdings-inc-insider-trades-uctt-stock-titan-2-1-insider-ownership-as-of-july-1-2025.html) [link to TipRanks UCTT Ownership](https://www.tipranks.com/stocks/uctt/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company carries a significant amount of debt, which it has used to finance large acquisitions that have broadened its product portfolio and customer base. [pos]Ultra Clean Holdings reported $317.6 million in total cash. Total debt is approximately $646.4 million. As of December 2024, gross debt was $499.7 million. The company has a current ratio of 3.03. A share repurchase program of up to $150.0 million was approved in 2022, with 1.1 million shares repurchased for $29.4 million in 2023 and 0.3 million shares for $12.1 million in 2022.[/pos] [link to Ultra Clean Holdings Q1 2025 Earnings Release](https://ir.uct.com/news-releases/news-release-details/2025/Ultra-Clean-Holdings-Inc.-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to Simply Wall St UCTT Financials](https://simplywall.st/stocks/us/semiconductors/nasdaq-uctt/ultra-clean-holdings/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Scalability is directly tied to the capital spending cycles of the semiconductor industry. It scales by deepening its relationships with major equipment makers like Applied Materials and Lam Research, and by providing a larger share of the components for each tool."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Ultra Clean Holdings entry updated successfully.")
