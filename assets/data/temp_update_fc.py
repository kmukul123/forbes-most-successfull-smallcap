

import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Franklinvey":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """FranklinCovey is a global company specializing in performance improvement. It helps organizations and individuals achieve results that require a change in human behavior through consulting, training, and its 'All Access Pass' subscription service. [highlight]Franklin Covey's competitive moat is built on its strong brand (The 7 Habits of Highly Effective People), proprietary intellectual property, expertise in human behavior change, global presence, and integrated solutions (All Access Pass). GuruFocus assesses it with a \"Narrow Moat.\"[/highlight] [pos]Franklin Covey has a Return on Invested Capital (ROIC) of 36.27% (Financial Modeling Prep, as of February 2025). Its TTM ROIC was 8.91%.[/pos] [link to Franklin Covey Investor Relations](https://ir.franklincovey.com/) [link to Financial Modeling Prep FC ROIC](https://financialmodelingprep.com/financial-statements/FC) [link to GuruFocus FC ROIC](https://www.gurufocus.com/term/roic/NYSE:FC)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership is significant, with WallStreetZen reporting 68.01% (or 47.08%) and GuruFocus reporting 24.96%. The CEO and other key executives hold a substantial number of shares. Insiders have actively engaged in share buybacks.[/pos] [link to WallStreetZen FC Ownership](https://www.wallstreetzen.com/stocks/us/consumer-services/nyse-fc/franklin-covey/ownership) [link to GuruFocus FC Ownership](https://www.gurufocus.com/term/insider_ownership/NYSE:FC)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company maintains a strong balance sheet with very little debt, allowing it to invest in content and technology. [pos]Franklin Covey reported $33.71 million in cash and cash equivalents, with total debt of $2.35 million, resulting in a net cash position of $31.36 million. The company has actively engaged in share buyback programs, with a new $50 million plan approved in April 2024. Its diluted shares outstanding have remained relatively stable, indicating that buybacks have offset potential dilution.[/pos] [link to Franklin Covey Q1 2025 Earnings Release](https://ir.franklincovey.com/news-releases/news-release-details/2025/FranklinCovey-Reports-First-Quarter-Fiscal-2025-Results/default.aspx) [link to StockAnalysis FC Financials](https://stockanalysis.com/stocks/fc/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Highly scalable due to its shift to the 'All Access Pass' subscription model, which provides recurring revenue and high margins. It scales by signing more enterprise clients to the pass and expanding its digital content library."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Franklinvey entry updated successfully.")

