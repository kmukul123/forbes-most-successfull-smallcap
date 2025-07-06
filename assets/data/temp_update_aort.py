

import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Artivion":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Artivion is a medical device company focused on developing solutions for the treatment of aortic disease. Its products include aortic stents, surgical grafts, and tissue-based products used in cardiac and vascular surgery. [highlight]Artivion's competitive moat is built on its robust intellectual property portfolio (37 issued patents in 2022, 83 active patents in 2024), specialized expertise in cardiovascular surgical technologies, and established relationships within the medical community. It has FDA-approved devices across seven primary product lines and a global distribution network across 37 countries.[/highlight] [neg]However, its ROCE and ROIC have shown fluctuations and generally low returns. Morningstar assigns a \"None\" economic moat rating.[/neg] [pos]Artivion has a Return on Capital Employed (ROCE) of 0.45% and a Return on Invested Capital (ROIC) of 0.57% (StockAnalysis, 2025). Its annualized ROIC was 0.26% as of March 2025.[/pos] [link to Artivion Investor Relations](https://www.artivion.com/investors/) [link to StockAnalysis AORT ROIC/ROCE](https://stockanalysis.com/stocks/aort/roic/) [link to GuruFocus AORT ROIC](https://www.gurufocus.com/term/roic/NYSE:AORT)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership is present but modest, with TipRanks reporting 5.60% and Trendlyne indicating a slight decrease from 6.79% to 6.68% in June 2025. Insiders have both bought and sold shares recently.[/pos] [link to TipRanks AORT Ownership](https://www.tipranks.com/stocks/aort/ownership) [link to Trendlyne AORT Insider Trading](https://trendlyne.com/equity/share-holding/1400/AORT/latest/artivion-inc/)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company carries a significant amount of debt, which it has used to fund key acquisitions and the clinical development of its innovative aortic arch remodeling products. [pos]As of March 31, 2025, Artivion had $14.5 million in cash and equivalents. Its Debt/Equity ratio is 1.23.[/pos] [neg]The company has experienced stock dilution. In May 2025, Artivion exchanged approximately $99.5 million in principal amount of its 4.250% Convertible Senior Notes due 2025 for common stock, resulting in the issuance of approximately 4.1 million new shares. The number of shares outstanding increased by 2.33% in one year. There is no indication of recent share buyback programs.[/neg] [link to Artivion Q1 2025 Earnings Release](https://www.artivion.com/news-releases/news-release-details/2025/Artivion-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to StockAnalysis AORT Shares Outstanding](https://stockanalysis.com/stocks/aort/shares-outstanding/)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """High scalability potential, driven by its leadership position in the specialized field of aortic repair. Growth comes from the commercialization of new, high-margin products, international expansion, and training surgeons on its advanced procedures."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Artivion entry updated successfully.")
