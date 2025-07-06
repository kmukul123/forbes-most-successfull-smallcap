
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "PubMatic, Inc. Class A":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """PubMatic provides a cloud infrastructure platform for the digital advertising supply chain. It offers a sell-side platform (SSP) that enables publishers to monetize their ad inventory and allows advertisers to reach audiences in real-time. [highlight]PubMatic's competitive moat is built on its owned and operated infrastructure (lower costs, greater control), AI-driven optimization, focus on premium inventory, continuous product innovation (CTV, Activate, Connect), Supply Path Optimization (SPO), consistent profitability, and high customer retention.[/highlight] [pos]As of March 2025, PubMatic's Return on Capital Employed (ROCE) was -0.77% and Return on Invested Capital (ROIC) was -20.09% (GuruFocus).[/pos] [neg]The low and negative ROIC/ROCE figures suggest that the company is not generating returns that exceed its cost of capital, potentially leading to value destruction as it grows.[/neg] [link to PubMatic Investor Relations](https://investors.pubmatic.com/) [link to GuruFocus PUBM ROIC](https://www.gurufocus.com/term/roic/NASDAQ:PUBM) [link to StockAnalysis PUBM ROIC/ROCE](https://stockanalysis.com/stocks/pubm/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Founders and executives retain a significant ownership stake and voting control, ensuring a stable and long-term strategic direction. Insider ownership is approximately 0.45% (TipRanks) to 1.19% (GuruFocus).[/pos] [link to TipRanks PUBM Ownership](https://www.tipranks.com/stocks/pubm/ownership) [link to GuruFocus PUBM Ownership](https://www.gurufocus.com/term/insider_ownership/NASDAQ:PUBM)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """PubMatic operates with no debt and has a strong cash position, allowing for continuous investment in its technology infrastructure and global operations. [pos]As of March 31, 2025, cash and cash equivalents were $144.13 million, with no debt. The company had a net cash position of $98.79 million.[/pos] [pos]PubMatic has an active stock repurchase program. In May 2025, the board authorized a $100 million increase to the program, bringing the total to $130.8 million through December 2026. As of March 31, 2025, $138.2 million had been used to repurchase 8.7 million shares (17% of fully diluted shares) since program inception. The company has been actively repurchasing shares, leading to a decrease in diluted shares outstanding in recent years, indicating a commitment to returning value to shareholders and potentially reducing dilution.[/pos] [link to PubMatic Q1 2025 Earnings Release](https://investors.pubmatic.com/news-releases/news-release-details/2025/PubMatic-Announces-First-Quarter-2025-Financial-Results/default.aspx) [link to TipRanks PUBM Buybacks](https://www.tipranks.com/stocks/pubm/buybacks)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Highly scalable platform. Growth is driven by the increasing adoption of programmatic advertising, especially in high-growth formats like connected TV and mobile video. It scales by processing more ad impressions and expanding its relationships with global publishers and advertisers."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("PubMatic, Inc. Class A entry updated successfully.")
