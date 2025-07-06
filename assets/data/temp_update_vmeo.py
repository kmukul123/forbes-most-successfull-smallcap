

import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Vimeo":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Vimeo is an all-in-one video software solution, providing creative professionals, businesses, and organizations with the tools to create, manage, and share high-quality videos. It operates as a SaaS platform, distinguishing itself from ad-supported platforms like YouTube. [highlight]Vimeo's competitive moat is built on its focus on high-quality, ad-free video experiences, robust tools for creators and businesses (AI-driven creation, OTT streaming, interactive video), and a subscription-based model. It offers professional-grade features and a \"Showcase\" feature for branded presentations.[/highlight] [neg]However, Morningstar assigns \"Economic Moat: None,\" and it faces challenges from larger competitors and stagnant revenue growth.[/neg] [pos]Vimeo has a Return on Invested Capital (ROIC) of 1.80% and a Return on Capital Employed (ROCE) of 2.93% (StockAnalysis). Its annualized ROIC for Q1 2025 was -6.06%, and TTM ROIC was 1.62%.[/pos] [link to Vimeo Investor Relations](https://investors.vimeo.com/) [link to StockAnalysis VMEO ROIC/ROCE](https://stockanalysis.com/stocks/vmeo/roic/) [link to GuruFocus VMEO ROIC](https://www.gurufocus.com/term/roic/NASDAQ:VMEO)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership is modest, with TipRanks reporting 3.66% and Fintel reporting 6.83%.[/pos] [link to TipRanks VMEO Ownership](https://www.tipranks.com/stocks/vmeo/ownership) [link to Fintel VMEO Ownership](https://fintel.io/n/us/vmeo)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company maintains a strong balance sheet with a healthy cash position and no significant debt, allowing it to invest in its platform and features. [pos]As of September 30, 2024, Vimeo reported $324.8 million in cash and cash equivalents and no debt. The company has an ongoing share repurchase program, with a new $50 million program announced in May 2025. In 2024, 5.9 million shares were repurchased for $26.8 million. However, diluted shares outstanding have shown an increasing trend, with a 2.53% increase in 2024, indicating some dilution despite buyback efforts.[/pos] [link to Vimeo Q1 2025 Earnings Release](https://investors.vimeo.com/news-releases/news-release-details/2025/Vimeo-Announces-First-Quarter-2025-Financial-Results/default.aspx) [link to Vimeo Share Repurchase Program](https://investors.vimeo.com/news-releases/news-release-details/2025/Vimeo-Announces-New-Share-Repurchase-Program/default.aspx)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Highly scalable SaaS model. Growth is driven by the increasing use of video for business communication, marketing, and training. It scales by converting free users to paid subscribers and by moving customers up to higher-tier enterprise plans."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Vimeo entry updated successfully.")
