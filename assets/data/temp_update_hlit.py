

import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Harmonic":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Harmonic provides video delivery technology and services. Its solutions enable media companies and service providers to deliver high-quality video streaming and broadcast services to consumers globally. It is a leader in virtualized cable access (vCMTS) and video SaaS. [highlight]Harmonic's competitive moat is built on its leadership in virtualized broadband solutions (cOS™ platform), technological innovation (HEVC, streaming, fiber rollouts), strategic partnerships (e.g., Akamai), and operational efficiency. GuruFocus suggests a \"Narrow Moat,\" though Morningstar assigns \"None.\"[/highlight] [pos]Harmonic has a Return on Capital Employed (ROCE) of 18.02% and a Return on Invested Capital (ROIC) of 11.83% (StockAnalysis). Its ROCE was 15% for the trailing twelve months to December 2024.[/pos] [link to Harmonic Investor Relations](https://www.harmonicinc.com/investor-relations/) [link to StockAnalysis HLIT ROIC/ROCE](https://stockanalysis.com/stocks/hlit/roic/) [link to GuruFocus HLIT ROIC](https://www.gurufocus.com/term/roic/NASDAQ:HLIT)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership is modest, with MarketBeat reporting 1.21% and TipRanks reporting 1.42%. Insiders have bought more shares than they have sold in the last three months.[/pos] [link to MarketBeat HLIT Ownership](https://www.marketbeat.com/stocks/NASDAQ/HLIT/institutional-ownership/) [link to TipRanks HLIT Ownership](https://www.tipranks.com/stocks/hlit/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company carries a moderate amount of debt, often in the form of convertible notes, to fund its strategic shift towards software and cloud-based solutions. [pos]As of March 2025, Harmonic reported $148.7 million in cash and cash equivalents, with $127.9 million in debt, resulting in a net cash position of $20.8 million. Its debt-to-equity ratio decreased from 64.3% to 28.7% over the past five years. Debt is well-covered by operating cash flow (92.8%) and interest payments are covered 13.6 times by EBIT.[/pos] [link to Simply Wall St HLIT Financials](https://simplywall.st/stocks/us/technology/nasdaq-hlit/harmonic/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Highly scalable, particularly its software and SaaS businesses. Growth is driven by the global transition to streaming video and the upgrade of cable networks to new, faster standards (DOCSIS 4.0). Its CableOS software platform is a key driver of scalable, recurring revenue."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Harmonic entry updated successfully.")

