import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Interface":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Interface is a global leader in the design and manufacturing of modular carpet tiles. The company also offers other flooring products like luxury vinyl tile (LVT) and rubber flooring, with a strong focus on sustainability and carbon-neutral products. [highlight]Interface possesses a \"Narrow Moat\" (GuruFocus) built on its strong brand reputation and sustainability leadership (Mission Zero, Carbon Neutral Floors), continuous product innovation, global manufacturing capabilities and distribution network, and product diversification. It also benefits from cost advantages due to economies of scale and circular economy initiatives.[/highlight] [pos]Interface has a Return on Capital Employed (ROCE) of 12.93% and and a Return on Invested Capital (ROIC) of 8.72% (StockAnalysis). Its ROIC was 13.5% as of March 2025, with a 3-year average of 10.1% and a 5-year average of 7.9%.[/pos] [link to Interface Investor Relations](https://www.interface.com/na/en-us/about/investor-relations.html) [link to GuruFocus TILE Moat](https://www.gurufocus.com/term/moat/NASDAQ:TILE) [link to StockAnalysis TILE ROIC/ROCE](https://stockanalysis.com/stocks/tile/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership is modest, with GuruFocus reporting 12.58% and TipRanks reporting 3.11%. Key insiders include CEO Laurel M. Hurd. While there have been insider sales in the last 12 months, there have also been net purchases in the last 3 months.[/pos] [link to GuruFocus TILE Ownership](https://www.gurufocus.com/term/insider_ownership/NASDAQ:TILE) [link to TipRanks TILE Ownership](https://www.tipranks.com/stocks/tile/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company carries a moderate level of debt, which it has used to finance strategic acquisitions (like Nora Systems for rubber flooring) and invest in manufacturing. [pos]As of March 31, 2025, Interface had $97.76 million in cash and cash equivalents. Total debt was approximately $393.17 million, with a net cash position of -$295.41 million. The debt-to-equity ratio is 76.63%. Debt is well-covered by operating cash flow (48.7%) and interest payments are well covered by EBIT (6x coverage). In fiscal year 2024, the company repaid $115 million of debt.[/pos] [pos]Interface has an active share repurchase program, with $100 million authorized in May 2022. The company repurchased $17.2 million in 2022. Diluted weighted average shares have remained relatively stable, fluctuating between 58.5 million and 59.3 million shares from 2019 to 2025, indicating that buybacks have offset potential dilution.[/pos] [link to Interface Q1 2025 Earnings Release](https://investors.interface.com/news-releases/news-release-details/2025/Interface-Reports-First-Quarter-2025-Results/default.aspx) [link to StockAnalysis TILE Financials](https://stockanalysis.com/stocks/tile/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Scalability is tied to the commercial real estate market (office, hospitality, education). Growth comes from gaining market share, cross-selling its expanded product portfolio (carpet, LVT, rubber), and leading in the sustainable building materials space."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Interface entry updated successfully.")
