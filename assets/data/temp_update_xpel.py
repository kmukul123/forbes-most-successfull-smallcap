
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "XPEL":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """XPEL is a leading provider of protective films and coatings. Its products include automotive paint protection film (PPF), surface protection film, automotive and architectural window films, and ceramic coatings. [highlight]XPEL possesses a strong competitive moat built on its brand reputation, technological innovation (proprietary self-healing films, 37 patent applications), extensive distribution network with a certified installer ecosystem (over 4,500 locations), high customer satisfaction (99.2%) with robust warranties (7-10 years), significant market share (40% in US PPF), and high barriers to entry in the industry.[/highlight] [pos]XPEL has a Return on Invested Capital (ROIC) of 21.19% (GuruFocus, as of June 2025) and a Return on Capital Employed (ROCE) of 24.10% (StockAnalysis).[/pos] [link to XPEL Investor Relations](https://investors.xpel.com/) [link to GuruFocus XPEL ROIC](https://www.gurufocus.com/term/roic/NASDAQ:XPEL) [link to StockAnalysis XPEL ROIC/ROCE](https://stockanalysis.com/stocks/xpel/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]The CEO and founder holds a significant stake, ensuring strong leadership and alignment with long-term value creation. Insider ownership is approximately 9.50% (MarketBeat). Insiders have both bought and sold shares in the last 24 months.[/pos] [link to MarketBeat XPEL Ownership](https://www.marketbeat.com/stocks/NASDAQ/XPEL/institutional-ownership/)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company operates with a low level of debt, funding its growth through strong cash flow from operations. [pos]As of March 30, 2025, XPEL reported approximately $231.4 million in cash and short-term investments. Total debt was approximately $284.1 million. The company has a stable cash runway for more than three years based on its current free cash flow.[/pos] [pos]On May 6, 2025, XPEL announced a $50 million stock repurchase program, which could repurchase up to 5.4% of its outstanding shares. While shares outstanding have seen slight increases in recent years (e.g., 0.06% increase over the past year), the buyback program aims to counteract dilution.[/pos] [link to Simply Wall St XPEL Financials](https://simplywall.st/stocks/us/consumer-durables/nasdaq-xpel/xpel/financials) [link to XPEL Stock Repurchase Program](https://investors.xpel.com/news-releases/news-release-details/2025/XPEL-Announces-Stock-Repurchase-Program/default.aspx)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Highly scalable. Growth is driven by increasing consumer awareness and demand for vehicle protection, expanding its global installer network, and acquiring international distributors. Cross-selling its diverse product portfolio (PPF, window tint, ceramic coating) further enhances scalability."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("XPEL entry updated successfully.")
