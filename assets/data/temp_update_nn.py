

import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "NextNav":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """NextNav is a leader in next-generation GPS technology. It provides highly accurate, floor-level vertical positioning (z-axis) through its Pinnacle network and resilient position, navigation, and timing (PNT) services through its TerraPoiNT network. [highlight]NextNav's competitive moat is built on its niche specialization in vertical positioning (z-axis), proprietary and patented technology (MBS, TerraPoiNT systems, over 100 patents), regulatory tailwinds (FCC E911 requirements), and strategic assets (8 MHz of low-band spectrum, deployed network in over 4,400 cities).[/highlight] [neg]However, Morningstar assesses its economic moat as \"None.\"[/neg] [pos]NextNav has a Return on Capital Employed (ROCE) of -46.2% and a Return on Invested Capital (ROIC) of -65.6% (FullRatio). Stock Analysis reports ROIC as -21.09% and ROCE as -23.71%.[/pos] [link to NextNav Investor Relations](https://nextnav.com/investors/) [link to FullRatio NN ROIC/ROCE](https://fullratio.com/stocks/NN/roic) [link to StockAnalysis NN ROIC/ROCE](https://stockanalysis.com/stocks/nn/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership includes stakes from its founders, management, and strategic investors from the telecom and technology sectors. Insider ownership is approximately 7.70% (MarketBeat) to 15.91% (TipRanks). As of October 2024, insiders owned 24% of the company, with insider buying outpacing selling over the past year.[/pos] [link to MarketBeat NN Ownership](https://www.marketbeat.com/stocks/NASDAQ/NN/institutional-ownership/) [link to TipRanks NN Ownership](https://www.tipranks.com/stocks/nn/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company has funded the build-out of its networks and technology development through significant equity investment and carries a manageable level of debt. [pos]As of March 31, 2025, NextNav reported 131.104 million diluted shares outstanding, an 18.05% increase from the previous year, indicating significant stock dilution. This is partly due to a $50 million debt financing in May 2023 and a private placement of $190 million in convertible notes in March 2025. There is no clear indication of significant share repurchase programs.[/pos] [link to NextNav Q1 2025 Earnings Release](https://nextnav.com/news-releases/news-release-details/2025/NextNav-Announces-First-Quarter-2025-Financial-Results/default.aspx) [link to Finance Charts NN Shares Outstanding](https://financecharts.com/stocks/nn/shares-outstanding/)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Extremely high scalability. The value of its technology and spectrum licenses is immense. Growth is driven by the adoption of its services by mobile app developers, wireless carriers, and government agencies for E911 and public safety. Monetization of its spectrum provides another significant scalability path."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("NextNav entry updated successfully.")
