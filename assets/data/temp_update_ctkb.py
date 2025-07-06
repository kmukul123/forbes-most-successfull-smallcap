

import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Cytek Biosciences":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Cytek Biosciences is a cell analysis solutions company that provides compact, high-performance flow cytometry instruments. Its technology allows scientists and clinicians to perform more complex cell analysis, which is critical for immunology and cancer research. [highlight]Cytek Biosciences' competitive moat is built on its proprietary Full Spectrum Profiling (FSP) technology (high-resolution, high-content, high-sensitivity), robust intellectual property (41+ patents), significant R&D investment, market leadership in full spectrum flow cytometry, comprehensive solution offerings (instruments, consumables, software, services), and a customer-centric approach.[/highlight] [neg]However, Morningstar assesses it as having \"No Economic Moat.\"[/neg] [pos]Cytek Biosciences has a Return on Capital Employed (ROCE) of -6.60% and a Return on Invested Capital (ROIC) of -4.26% (StockAnalysis). Its annualized ROIC for Q1 2025 was -4.92%.[/pos] [link to Cytek Biosciences Investor Relations](https://ir.cytekbio.com/) [link to StockAnalysis CTKB ROIC/ROCE](https://stockanalysis.com/stocks/ctkb/roic/) [link to GuruFocus CTKB ROIC](https://www.gurufocus.com/term/roic/NASDAQ:CTKB)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Founders, management, and early-stage investors hold a significant stake. Insider ownership is approximately 9.19% (MarketBeat) to 10.33% (TipRanks).[/pos] [link to MarketBeat CTKB Ownership](https://www.marketbeat.com/stocks/NASDAQ/CTKB/institutional-ownership/) [link to TipRanks CTKB Ownership](https://www.tipranks.com/stocks/ctkb/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company has a strong, debt-free balance sheet with a large cash position from its IPO, which it is using to fund R&D and commercial expansion. [pos]As of March 31, 2025, Cytek Biosciences reported $265.6 million in cash and marketable securities. Total debt was $5.71 million as of December 2024, resulting in a net cash position of $272.2 million. The company has an active stock repurchase program, with a new $50 million program approved for 2025. Its diluted shares outstanding decreased by 1.97% from March 2024 to March 2025, indicating a reduction in shares through buybacks.[/pos] [link to Cytek Biosciences Q1 2025 Earnings Release](https://ir.cytekbio.com/news-releases/news-release-details/2025/Cytek-Biosciences-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to Finance Charts CTKB Shares Outstanding](https://financecharts.com/stocks/ctkb/shares-outstanding/)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Highly scalable 'razor-and-blade' model. It sells instruments (the 'razor') and generates recurring revenue from proprietary reagents and software (the 'blades'). Growth is driven by placing more instruments in research labs and by increasing the usage of its high-margin consumables."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Cytek Biosciences entry updated successfully.")
