import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Red Violet Spn":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Red Violet is a data and analytics company that provides a cloud-based platform, 'idore', for data fusion and analytics. Its solutions are used by various industries for risk management, fraud detection, due diligence, and identity verification. [highlight]Red Violet's competitive moat is built on its proprietary CORE™ platform (data fusion, real-time capabilities), differentiated data assets, specialization in niche markets, and increasing AI integration for predictive analytics. Its subscription-based and usage-based revenue model ensures recurring revenue. The FOREWARN application, designed for realtor safety, demonstrates its ability to dominate specific industry verticals.[/highlight] [pos]Red Violet had a Return on Invested Capital (ROIC) of 22.51% as of March 2025, with a trailing twelve months (TTM) ROIC of 13.31%.[/pos] [link to Red Violet Investor Relations](https://ir.redviolet.com/) [link to GuruFocus RDVT ROIC](https://www.gurufocus.com/term/roic/NASDAQ:RDVT)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]The company has very high insider ownership, with its Chairman and other key executives holding a majority of the stock, indicating deep conviction in the business. Insider ownership is approximately 20% (MarketBeat) to 27.24% (Stock Titan). Roger E. Susi, the CEO, holds a significant stake.[/pos] [link to MarketBeat RDVT Ownership](https://www.marketbeat.com/stocks/NASDAQ/RDVT/institutional-ownership/) [link to Stock Titan RDVT Ownership](https://stocktitan.net/news/RDVT/red-violet-inc-insider-trades-rdvt-stock-titan-27-24-insider-ownership-as-of-july-1-2025.html)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company is debt-free and funds its operations and growth initiatives through its revenue and cash reserves. [pos]As of March 31, 2025, Red Violet reported approximately $34.6 million in cash and cash equivalents, with total debt around $1.85 million, resulting in a net cash position of approximately $32.76 million.[/pos] [pos]Red Violet has actively engaged in share repurchase programs, allocating $15.0 million to its program since May 2022, and repurchasing 538,484 shares for $10.4 million. An additional $5.0 million was authorized in December 2023. The company also paid a special cash dividend of $0.30 per share in February 2025. There is no explicit information indicating recent stock dilutions.[/pos] [link to Red Violet Q1 2025 Earnings Release](https://ir.redviolet.com/news-releases/news-release-details/2025/Red-Violet-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to Red Violet Investor Relations - Share Repurchase](https://ir.redviolet.com/news-releases/news-release-details/2024/Red-Violet-Announces-Special-Cash-Dividend-and-Share-Repurchase-Program-Update/default.aspx)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Highly scalable SaaS business model. Growth comes from acquiring new customers in various verticals (legal, financial services, government), increasing usage among existing customers, and developing new data analytics products."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Red Violet Spn entry updated successfully.")