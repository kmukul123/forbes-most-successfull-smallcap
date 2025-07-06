

import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Innoviva":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Innoviva manages a portfolio of royalty-bearing assets in the healthcare sector. Its primary source of revenue comes from royalties on respiratory therapies developed in partnership with GlaxoSmithKline (GSK), such as Relvar/Breo Ellipta. [highlight]Innoviva's competitive moat is built on its established royalty revenue streams (high gross profit margins), strategic partnerships (e.g., GSK), diversification into specialty therapeutics, and differentiated expertise in asset monetization. Morningstar assesses its economic moat as \"Narrow.\"[/highlight] [pos]Innoviva's Return on Invested Capital (ROIC) is 24.05% (GuruFocus, TTM as of June 8, 2025), and its Return on Capital Employed (ROCE) is 18.61% (Stock Analysis).[/pos] [link to Innoviva Investor Relations](https://inva.com/investor-relations/) [link to GuruFocus INVA ROIC](https://www.gurufocus.com/term/roic/NASDAQ:INVA) [link to StockAnalysis INVA ROIC/ROCE](https://stockanalysis.com/stocks/inva/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership is approximately 10.20%, with directors and executive officers holding shares, indicating alignment of management interests with shareholders.[/pos] [link to TipRanks INVA Ownership](https://www.tipranks.com/stocks/inva/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company has a leveraged balance sheet, having used debt to fund acquisitions and provide returns to shareholders. Its stable royalty income supports its debt service. [pos]As of March 31, 2025, cash and cash equivalents were $178.4 million. As of May 2025, cash and marketable securities were just under $320 million, with debt just over $450 million. The debt-to-equity ratio as of March 31, 2025, was 0.40.[/pos] [pos]Innoviva has engaged in significant share repurchases, including 32 million shares from GSK in May 2021 for $392 million, and authorized a new $100 million buyback program in November 2022. Shares outstanding decreased from 69.2 million in 2022 to 62.771 million in March 2025, reflecting these efforts.[/pos] [link to Innoviva Q1 2025 Earnings Release](https://inva.com/investor-relations/news-releases/news-release-details/2025/Innoviva-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to Nasdaq INVA SEC Filings](https://www.nasdaq.com/market-activity/stocks/inva/sec-filings)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Scalable through the acquisition of new royalty streams and strategic investments in other healthcare assets. The business model is lean and does not require large operational overhead, making it efficient at scaling its portfolio."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Innoviva entry updated successfully.")
