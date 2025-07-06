
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Heidrick & Struggles Intl":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Heidrick & Struggles is a premier global provider of executive search, leadership consulting, and on-demand talent solutions. It helps organizations build strong leadership teams by finding and developing top-level executives. [highlight]Heidrick & Struggles' competitive moat is built on its focus on top-tier executive search, global presence (34 offices across 6 continents) with unified teams, strong brand and reputation (ranked #1 in Global Executive Search by Kennedy), extensive consultant network (500+ senior-level), and diversified service offerings (leadership advisory, on-demand talent).[/highlight] [neg]However, some analyses suggest it lacks traditional competitive moats like significant IP or regulatory barriers.[/neg] [pos]Heidrick & Struggles Intl has a Return on Capital Employed (ROCE) of 11.45% and a Return on Invested Capital (ROIC) of 8.52% (StockAnalysis). Its ROIC was 4.28% (GuruFocus, TTM as of July 2025), with a 3-year average of 14.60%.[/pos] [link to Heidrick & Struggles Investor Relations](https://www.heidrick.com/investors) [link to StockAnalysis HSII ROIC/ROCE](https://stockanalysis.com/stocks/hsii/roic/) [link to GuruFocus HSII ROIC](https://www.gurufocus.com/term/roic/NASDAQ:HSII)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership varies across sources, from 1.43% (MarketBeat) to 9.26% (Fintel). Ronald N. Tutor is the largest individual shareholder, owning 44.15% of the company. Insiders have both bought and sold shares recently.[/pos] [link to MarketBeat HSII Ownership](https://www.marketbeat.com/stocks/NASDAQ/HSII/institutional-ownership/) [link to Fintel HSII Ownership](https://fintel.io/n/us/hsii)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company maintains a strong, debt-free balance sheet, which provides stability through economic cycles. [pos]Heidrick & Struggles International reported $324.66 million in total cash and $100.09 million in total debt. As of Q1 2025, cash was $325 million. The company has a stock repurchase program ($50 million authorized in February 2008). In 2023, 36,000 shares were repurchased. Its diluted EPS was $0.37 (TTM as of July 2025).[/pos] [link to Heidrick & Struggles Q1 2025 Earnings Release](https://www.heidrick.com/newsroom/press-releases/2025/Heidrick-Struggles-Reports-First-Quarter-2025-Results) [link to StockAnalysis HSII Financials](https://stockanalysis.com/stocks/hsii/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Scalable by adding more high-performing search consultants and by cross-selling its leadership advisory and on-demand talent services to its blue-chip client base. The business is cyclical but highly profitable at scale."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Heidrick & Struggles Intl entry updated successfully.")
