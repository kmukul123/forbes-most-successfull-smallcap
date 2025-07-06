

import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "ReposiTrak":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """ReposiTrak, a subsidiary of Park City Group, operates a cloud-based B2B platform for the retail supply chain. Its solutions include compliance management, food safety, supply chain visibility, and out-of-stock prevention. [highlight]ReposiTrak's competitive moat is built on its extensive network effects (world's largest food traceability and compliance network with over 30,000 suppliers), regulatory tailwinds (FDA FSMA 204), proprietary SaaS platform, operational efficiency through automation, and high profitability (gross margins often exceeding 83%). Morningstar assesses it as having a \"Narrow Moat.\"[/highlight] [pos]ReposiTrak has a Return on Capital Employed (ROCE) of 12.07% and a Return on Invested Capital (ROIC) of 21.33% (GuruFocus, TTM as of June 2025).[/pos] [link to ReposiTrak Investor Relations](https://repositrak.com/investors/) [link to GuruFocus TRAK ROIC](https://www.gurufocus.com/term/roic/NASDAQ:TRAK) [link to StockAnalysis TRAK ROIC/ROCE](https://stockanalysis.com/stocks/trak/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]The CEO and key executives have substantial ownership, indicating a strong belief in the platform's value proposition. Insider ownership varies across sources, from 31.5% (Simply Wall St) to 44.00% (MarketBeat). Randall K. Fields is a significant insider shareholder.[/pos] [link to MarketBeat TRAK Ownership](https://www.marketbeat.com/stocks/NASDAQ/TRAK/institutional-ownership/) [link to Simply Wall St TRAK Ownership](https://simplywall.st/stocks/us/software/nasdaq-trak/repositrak/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company is debt-free and has a strong cash position, allowing it to invest in enhancing its software platform and sales efforts. [pos]As of June 30, 2024, ReposiTrak reported $25.2 million in cash and no bank debt. Forbes reported $28.13 million in total cash and $780,000 in total debt as of November 2024. The company has a remaining authorization of approximately $8 million for common share buybacks and is in the process of redeeming all its preferred shares. Shares outstanding increased by 1.18% over the past year, indicating slight dilution despite buyback activities.[/pos] [link to ReposiTrak Q4 2024 Earnings Release](https://repositrak.com/news-releases/news-release-details/2024/ReposiTrak-Announces-Fourth-Quarter-and-Full-Year-2024-Financial-Results/default.aspx) [link to StockAnalysis TRAK Shares Outstanding](https://stockanalysis.com/stocks/trak/shares-outstanding/)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Very scalable SaaS model with strong network effects. As more retailers and suppliers join the platform, its value increases for all participants. Growth comes from expanding its network and upselling new software modules to its captive user base."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("ReposiTrak entry updated successfully.")
