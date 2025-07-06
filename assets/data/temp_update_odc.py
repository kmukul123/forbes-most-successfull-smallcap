
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Oil-Dri Corporation of America":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Oil-Dri Corporation of America develops, manufactures, and markets sorbent products from clay minerals. Its products include cat litter (Cat's Pride), industrial absorbents, agricultural chemical carriers, and purification aids for edible oils. [highlight]Oil-Dri's competitive moat is built on its ownership of unique clay mineral reserves, which provides a cost advantage and supply chain control. Its long history and established brand names (e.g., Cat's Pride) contribute to customer loyalty. The company also benefits from product innovation (e.g., lightweight cat litter) and diversification across various markets.[/highlight] [pos]Oil-Dri Corporation of America has a Return on Capital Employed (ROCE) of 4.47% and a Return on Invested Capital (ROIC) of 2.67% (StockAnalysis).[/pos] [link to Oil-Dri Investor Relations](https://www.oildri.com/investors) [link to StockAnalysis ODC ROIC/ROCE](https://stockanalysis.com/stocks/odc/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]The founding family maintains voting control of the company through a dual-class share structure, ensuring a very long-term perspective. Insider ownership varies across sources, from 2.77% (TipRanks) to 11.66% (MarketBeat). Insiders have sold more shares than they have purchased in the last three months.[/pos] [link to TipRanks ODC Ownership](https://www.tipranks.com/stocks/odc/ownership) [link to MarketBeat ODC Insider Trading](https://www.marketbeat.com/stocks/NYSE/ODC/insider-trades/)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company operates with a very low level of debt, maintaining a conservative financial posture that has supported its stability for decades. [pos]As of March 31, 2025, Oil-Dri Corporation of America reported $36.48 million in cash and cash equivalents, with total debt of $57.21 million, resulting in a net cash position of -$20.74 million. Its debt-to-equity ratio is 0.23. Debt is well covered by operating cash flow (192.1%) and interest payments are well covered by EBIT (31x coverage).[/pos] [pos]The company has actively repurchased shares, with $69,000 in buybacks in Q1 2025, and $2.778 million in 2024. A significant buyback plan in 2005 repurchased 9.14% of its stock. However, shares outstanding increased by 1.34% over the last year, indicating some dilution despite buyback activities.[/pos] [link to Forbes ODC Financials](https://www.forbes.com/companies/oil-dri/) [link to StockAnalysis ODC Financials](https://stockanalysis.com/stocks/odc/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Moderately scalable. Growth is driven by product innovation (e.g., lightweight cat litter), market share gains in its various segments, and international expansion. Its ownership of unique clay mineral reserves provides a strong competitive advantage."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Oil-Dri Corporation of America entry updated successfully.")
