
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Carriage Services":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Carriage Services is a provider of deathcare services and merchandise in the United States. It operates a portfolio of funeral homes and cemeteries, focusing on a decentralized model that allows local businesses to maintain their community identities. [highlight]Carriage Services' competitive moat is built on its extensive network (97 funeral homes, 29 cemeteries across 20 states), strategic acquisition strategy, focus on pre-need sales for revenue visibility, established brand, and technological integration. Its high fixed-asset business model provides strong operating leverage, and its services are recession-resistant.[/highlight] [pos]Carriage Services has a Return on Invested Capital (ROIC) of 7.29% and a Return on Capital Employed (ROCE) of 7.29% as of the past 12 months (StockAnalysis). Its ROIC was 6.35% as of June 2025, an improvement of 17.92% from its 3-year average.[/pos] [link to Carriage Services Investor Relations](https://www.carriageservices.com/investor-relations/) [link to StockAnalysis CSV ROIC/ROCE](https://stockanalysis.com/stocks/csv/roic/) [link to Finance Charts CSV ROIC](https://financecharts.com/stocks/csv/roic)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]The founder and CEO holds a significant stake in the company, promoting a long-term, shareholder-aligned vision. Insider ownership is approximately 20% (MarketBeat) to 27.24% (Stock Titan). Roger E. Susi, the CEO, holds a significant stake.[/pos] [link to MarketBeat CSV Ownership](https://www.marketbeat.com/stocks/NYSE/CSV/institutional-ownership/) [link to Stock Titan CSV Ownership](https://stocktitan.net/news/CSV/carriage-services-inc-insider-trades-csv-stock-titan-27-24-insider-ownership-as-of-july-1-2025.html)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company carries a substantial amount of debt, which it uses to finance its primary growth strategy of acquiring independent funeral homes and cemeteries. [pos]As of March 30, 2025, Carriage Services had approximately $4.6 million in cash and short-term investments. Total debt was reported as $520.7 million, with long-term debt at $419.3 million.[/pos] [link to Simply Wall St CSV Financials](https://simplywall.st/stocks/us/consumer-services/nyse-csv/carriage-services/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Scalable through a disciplined acquisition strategy in the highly fragmented deathcare industry. Growth is also supported by stable, demographically-driven demand and the ability to improve operations at acquired businesses."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Carriage Services entry updated successfully.")
