
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Sprinklr":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Sprinklr provides a unified customer experience management (Unified-CXM) software platform for enterprises. It helps large companies manage their marketing, advertising, customer service, and social media engagement across dozens of digital channels. [highlight]Sprinklr's competitive moat is built on its unified AI-powered platform, advanced AI and data analytics, enterprise focus and scalability, omnichannel integration (30+ channels), strong customer success strategy, and strategic partnerships with major digital platforms.[/highlight] [pos]Sprinklr has a Return on Capital Employed (ROCE) of 5.13% (StockAnalysis). Its annualized ROIC for Q1 2025 was -2.32%, and TTM ROIC was 13.20% (GuruFocus).[/pos] [link to Sprinklr Investor Relations](https://investors.sprinklr.com/) [link to StockAnalysis CXM ROIC/ROCE](https://stockanalysis.com/stocks/cxm/roic/) [link to GuruFocus CXM ROIC](https://www.gurufocus.com/term/roic/NYSE:CXM)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]The founder and CEO holds a significant ownership stake and voting control, ensuring a consistent, long-term vision for the platform. Insider ownership is approximately 60.53% (MarketBeat) or 8.63% (dcfmodeling.com).[/pos] [link to MarketBeat CXM Ownership](https://www.marketbeat.com/stocks/NYSE/CXM/institutional-ownership/)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company has a strong balance sheet with a large cash position and no significant debt, allowing for continued investment in its enterprise-grade platform. [pos]As of June 5, 2025, Sprinklr reported approximately $570 million in cash and marketable securities, with no debt. The company has actively engaged in share buybacks, with a new $150 million program approved in June 2025 (concluding June 2026). In Q4 2024, $173.889 million in shares were repurchased. The company completed a $300 million authorization in January 2025. Its diluted shares outstanding were 274 million as of January 2025, with a projected 277 million for FY 2026.[/pos] [link to Sprinklr Q1 2026 Earnings Release](https://investors.sprinklr.com/news-releases/news-release-details/2025/Sprinklr-Announces-First-Quarter-Fiscal-2026-Results/default.aspx) [link to Sprinklr Share Repurchase Program](https://investors.sprinklr.com/news-releases/news-release-details/2025/Sprinklr-Announces-New-Share-Repurchase-Program/default.aspx)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Highly scalable SaaS platform. Growth is driven by landing new large enterprise customers and expanding the number of software modules used by existing customers. The increasing complexity of managing digital customer experiences provides a strong tailwind."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Sprinklr entry updated successfully.")
