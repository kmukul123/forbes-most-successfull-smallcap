
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Mayville Engnering Cmpny":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Mayville Engineering Company (MEC) is a leading U.S.-based contract manufacturer. It provides a broad range of prototyping, engineering, production, and aftermarket services to a diverse set of OEM customers in markets like commercial vehicles, construction, and agriculture. [highlight]Mayville Engineering Company's competitive moat is built on its extensive manufacturing expertise (largest metal fabricator in U.S.), diverse market penetration, significant employee ownership (45% of company), strategic Tier 1 supplier status, investment in innovation (193 active patents), and broad geographic footprint (20 facilities).[/highlight] [pos]Mayville Engineering Company has a Return on Capital Employed (ROCE) of 3.90% and a Return on Invested Capital (ROIC) of 2.37% (StockAnalysis). Its ROIC has soared by 108% year-over-year, and its ROIC Ratio was 7.83% in December 2024, the highest in five years.[/pos] [link to MEC Investor Relations](https://ir.mecinc.com/) [link to StockAnalysis MEC ROIC/ROCE](https://stockanalysis.com/stocks/mec/roic/) [link to Finance Charts MEC ROIC](https://financecharts.com/stocks/mec/roic)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]The company was formerly employee-owned, and while now public, it retains a culture of shared ownership. Insider ownership is approximately 4.09% (TipRanks) to 6.65% (Fintel). Loren A. Unterseher owns the most shares. Insiders have both bought and sold shares recently.[/pos] [link to TipRanks MEC Ownership](https://www.tipranks.com/stocks/mec/ownership) [link to Fintel MEC Ownership](https://fintel.io/n/us/mec)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company carries a moderate amount of debt, which it uses to invest in advanced manufacturing technology and to finance strategic acquisitions. [pos]As of March 31, 2025, Mayville Engineering Company reported $80.6 million in outstanding debt, with $203.2 million in total cash and availability on its senior secured revolving credit facility. In Q1 2025, MEC repaid $2.5 million of debt. The company has an ongoing equity buyback program of up to $25 million through 2026. In Q1 2025, $1.7 million of common stock was repurchased. Its diluted average shares outstanding were 20.8 million as of June 2025, with stock-based compensation leading to some dilution.[/pos] [link to MEC Q1 2025 Earnings Release](https://ir.mecinc.com/news-releases/news-release-details/2025/Mayville-Engineering-Company-Inc.-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to Marketscreener MEC Buybacks](https://www.marketscreener.com/quote/stock/MAYVILLE-ENGINEERING-COMPANY-INC-47000000/news/Mayville-Engineering-Company-Inc-Announces-Share-Repurchase-Program-40000000/)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Scalable by deepening its relationships with its blue-chip OEM customers and by winning a larger share of their outsourced manufacturing needs. It also scales through acquisitions of smaller, specialized metal fabricators."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Mayville Engineering Company entry updated successfully.")
