
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Playags":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """PlayAGS is a designer and supplier of gaming products and services for the casino industry. Its offerings include slot machines, table game products, and interactive solutions for online and social gaming. [highlight]PlayAGS's competitive moat is built on its specialized gaming products, established relationships with casinos, and its ability to provide a comprehensive suite of gaming solutions. Its focus on high-growth segments like table games and interactive solutions further strengthens its position.[/highlight] [pos]Playags has a Return on Invested Capital (ROIC) of 16.8% (Value Sense) or 6.84% (StockAnalysis), and a Return on Capital Employed (ROCE) of 10.57% (StockAnalysis). Its 5-year average ROIC is 4.0%.[/pos] [link to PlayAGS Investor Relations](https://www.playags.com/investors/) [link to Value Sense AGS ROIC](https://valuesense.io/stocks/AGS/roic) [link to StockAnalysis AGS ROIC/ROCE](https://stockanalysis.com/stocks/ags/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[neg]As of June 30, 2025, Playags (AGS) insider ownership has dropped to zero due to the company's merger with Bingo Merger Sub, Inc., an affiliate of Brightstar Capital Partners. The company is now privately held.[/neg] [link to Stock Titan AGS Ownership](https://stocktitan.net/news/AGS/playags-inc-insider-trades-ags-stock-titan-0-insider-ownership-as-of-july-1-2025.html)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company operates with a significant amount of debt, a common characteristic for gaming equipment suppliers who finance their machine placements and development. [pos]As of March 6, 2025, PlayAGS reported cash and cash equivalents of $38.3 million. Total liabilities were $596.9 million, including $530.4 million in long-term debt.[/pos] [pos]PlayAGS has engaged in share buyback programs, with a $50 million program authorized in August 2019, extended until August 2025. As of March 31, 2024, $44.5 million remained available. The company repurchased 103,385 shares for $1.13 million under this program. Shares outstanding were 41,505,492 as of July 5, 2025.[/pos] [link to QZ.com AGS Financials](https://qz.com/news/2025-03-06-playags-inc-ags-reports-earnings-1852090000) [link to Marketscreener AGS Buybacks](https://www.marketscreener.com/quote/stock/PLAYAGS-INC-44900000/news/PlayAGS-Inc-Announces-Share-Repurchase-Program-29300000/)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Scalable by increasing its installed base of gaming machines in casinos, expanding into new gaming jurisdictions (both domestic and international), and growing its high-margin interactive and table games segments."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Playags entry updated successfully.")
