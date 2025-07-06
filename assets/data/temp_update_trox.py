
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Tronox":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Tronox Holdings is one of the world's leading vertically integrated producers of titanium dioxide (TiO2), a bright white pigment used in a wide range of products like paints, coatings, plastics, and paper. The company mines and processes its own titanium ore. [highlight]Tronox's competitive moat is built on its extensive vertical integration (mining to pigment production), global scale and footprint (plants and mines across six continents), low-cost production, product innovation, and sustainability initiatives. Its operational excellence further strengthens its position.[/highlight] [pos]Tronox has a Return on Invested Capital (ROIC) of 16.97% (GuruFocus, TTM as of June 2025) and a Return on Capital Employed (ROCE) of 2.51% (StockViz, TTM as of March 2025). Its ROIC was 1.98% as of March 2025. Its 5-year average ROIC is 8.3%.[/pos] [link to Tronox Investor Relations](https://investors.tronox.com/) [link to GuruFocus TROX ROIC](https://www.gurufocus.com/term/roic/NYSE:TROX) [link to StockAnalysis TROX ROIC/ROCE](https://stockanalysis.com/stocks/trox/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership is modest, with MarketBeat reporting 0.64% and TipRanks reporting 0.64%.[/pos] [link to MarketBeat TROX Ownership](https://www.marketbeat.com/stocks/NYSE/TROX/institutional-ownership/) [link to TipRanks TROX Ownership](https://www.tipranks.com/stocks/trox/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company operates with a high level of debt, a result of the major acquisitions it made to become a leading, vertically integrated player in the TiO2 industry. [pos]As of March 31, 2025, Tronox reported $138 million in cash and cash equivalents, with total debt of $3.0 billion and net debt of $2.8 billion. Its next significant debt maturity is not until 2029, and it has no financial covenants on its term loans or bonds. The company has engaged in stock buybacks, with $2.80 million in December 2024. A 1.3:1 stock split occurred in December 2013.[/pos] [link to Tronox Q1 2025 Earnings Release](https://investors.tronox.com/news-releases/news-release-details/2025/Tronox-Holdings-plc-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to Simply Wall St TROX Financials](https://simplywall.st/stocks/us/materials/nyse-trox/tronox/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Scalability is cyclical and tied to global GDP and industrial production. As a low-cost, integrated producer, it is well-positioned to benefit from rising TiO2 demand. Growth comes from optimizing its production assets and capitalizing on favorable market pricing."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Tronox entry updated successfully.")
