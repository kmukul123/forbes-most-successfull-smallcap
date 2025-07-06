

import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Xoma":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """XOMA has a unique business model focused on acquiring potential future royalty and milestone payments on partnered drug candidates. It has a large portfolio of assets licensed to other pharmaceutical companies, creating a diversified shot-on-goal model. [highlight]XOMA's competitive moat is built on its unique royalty-based business model, which allows it to acquire future economic rights to therapeutic products without the high costs and risks of drug development. It leverages proprietary antibody technologies and benefits from an experienced management team with strategic focus. However, GuruFocus suggests it has \"No Moat\" or \"Very weak/transient advantages.\"[/highlight] [pos]Xoma has a Return on Invested Capital (ROIC) of -7.28% and a Return on Capital Employed (ROCE) of -12.19% (StockAnalysis).[/pos] [link to Xoma Investor Relations](https://ir.xoma.com/) [link to StockAnalysis XOMA ROIC/ROCE](https://stockanalysis.com/stocks/xoma/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership is moderate, with MarketBeat reporting 7.20% and Trendlyne indicating an increase from 0.86% to 1.46% in May 2025. Insiders have both bought and sold shares recently.[/pos] [link to MarketBeat XOMA Ownership](https://www.marketbeat.com/stocks/NASDAQ/XOMA/institutional-ownership/) [link to Trendlyne XOMA Insider Trading](https://trendlyne.com/equity/share-holding/1400/XOMA/latest/xoma-corp/)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company operates with minimal debt, using its cash and equity to acquire new royalty assets. [pos]As of March 31, 2025, XOMA Royalty Corporation had $95.0 million in cash and cash equivalents. As of December 31, 2022, XOMA had no debt on its balance sheet. However, a Blue Owl Loan was established in December 2023. The number of shares outstanding has increased by 1.53% over the last year, indicating some dilution, but the company's business model is capital-efficient.[/pos] [link to XOMA Q1 2025 Earnings Release](https://ir.xoma.com/news-releases/news-release-details/2025/XOMA-Royalty-Corporation-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to StockAnalysis XOMA Shares Outstanding](https://stockanalysis.com/stocks/xoma/shares-outstanding/)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Highly scalable and capital-efficient model. It scales by acquiring more royalty assets without the high cost and risk of drug development. The value of the business grows as its partners advance the licensed drugs through clinical trials and toward commercialization."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Xoma entry updated successfully.")
