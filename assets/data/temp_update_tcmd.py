

import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Tactile Systems Technology":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Tactile Systems Technology (Tactile Medical) is a medical technology company that develops and provides at-home therapies for people with chronic diseases. Its primary products are advanced pneumatic compression devices for the treatment of lymphedema and chronic venous insufficiency. [highlight]Tactile Systems Technology's competitive moat is built on its proprietary technology and intellectual property (Flexitouch Plus system, acquired patents, licensed technologies), a direct-to-patient and clinician model, extensive health insurance coverage, clinically proven efficacy and cost-effectiveness, and regulatory barriers. It is a market leader in at-home therapy devices for chronic swelling conditions.[/highlight] [neg]However, Morningstar's quantitative rating suggests \"No Economic Moat.\"[/neg] [pos]Tactile Systems Technology has a Return on Capital Employed (ROCE) of 8.41% and a Return on Invested Capital (ROIC) of 5.24% (StockAnalysis). Its ROIC was 9.18% (GuruFocus, TTM).[/pos] [link to Tactile Systems Technology Investor Relations](https://www.tactilemedical.com/investors/) [link to StockAnalysis TCMD ROIC/ROCE](https://stockanalysis.com/stocks/tcmd/roic/) [link to GuruFocus TCMD ROIC](https://www.gurufocus.com/term/roic/NASDAQ:TCMD)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership varies across sources, from 2.50% (MarketBeat) to 28.01% (WallStreetZen). Jordan Davis is the largest individual shareholder (10.36%).[/pos] [link to WallStreetZen TCMD Ownership](https://www.wallstreetzen.com/stocks/us/medical-devices/nasdaq-tcmd/tactile-systems-technology/ownership) [link to MarketBeat TCMD Ownership](https://www.marketbeat.com/stocks/NASDAQ/TCMD/institutional-ownership/)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company maintains a strong balance sheet with minimal debt, allowing it to invest in its sales force and clinical research. [pos]As of March 31, 2025, Tactile Systems Technology reported $83.6 million in cash and $25.5 million in outstanding borrowings under its credit agreement. As of December 31, 2024, it had $94.4 million in cash and $26.2 million in debt, resulting in a net cash position of $68.2 million. The company has a share repurchase program of up to $30 million (valid until October 2026), with $10.0 million repurchased in Q1 2025. Diluted shares outstanding have shown an increasing trend (e.g., 24.102 million TTM).[/pos] [link to Tactile Systems Technology Q1 2025 Earnings Release](https://www.tactilemedical.com/news-releases/news-release-details/2025/Tactile-Systems-Technology-Inc.-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to Simply Wall St TCMD Financials](https://simplywall.st/stocks/us/medical-devices/nasdaq-tcmd/tactile-systems-technology/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Scalable by expanding its direct-to-patient and provider sales force, increasing awareness of the conditions it treats, and securing broader reimbursement coverage from payers. The large, undertreated patient population provides a long runway for growth."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Tactile Systems Technology entry updated successfully.")

