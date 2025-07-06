
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Collegium Pharmaceutical":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Collegium Pharmaceutical is a specialty pharmaceutical company focused on developing and commercializing medicines for pain management. Its portfolio is built around its proprietary DETERx platform, designed to create abuse-deterrent medications. [highlight]Its competitive moat is primarily built on its patented DETERx™ technology platform, which enables abuse-deterrent, extended-release formulations of pain medications, and its extensive intellectual property portfolio (19 Orange Book-listed patents for Xtampza ER through 2036).[/highlight] [pos]As of March 2025, Collegium reported a Return on Invested Capital (ROIC) of 5.32% (annualized) and a Return on Capital Employed (ROCE) of 8.32% (annualized).[/pos] [link to Collegium Pharma Investor Relations](https://ir.collegiumpharma.com/) [link to GuruFocus COLL ROIC/ROCE](https://www.gurufocus.com/term/roic/NASDAQ:COLL)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership is substantial, with WallStreetZen reporting 86.99% and David Hirsch holding 20.03% of shares, indicating strong alignment with shareholder interests. Other sources report lower figures (e.g., TipRanks 3.49%, GuruFocus 6.66%).[/pos] [link to WallStreetZen COLL Ownership](https://www.wallstreetzen.com/stocks/us/nasdaq/coll/insider-trading) [link to TipRanks COLL Ownership](https://www.tipranks.com/stocks/coll/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company has utilized convertible notes and other forms of debt to finance acquisitions and commercial activities but has been actively paying down its debt using its strong cash flow. [pos]As of March 31, 2025, Collegium had cash, cash equivalents, and marketable securities of $197.8 million.[/pos] [neg]As of September 2024, total debt was $867.2 million, resulting in a net debt of approximately $722.3 million.[/neg] [link to Collegium Pharma Q1 2025 Earnings Release](https://ir.collegiumpharma.com/news-releases/news-release-details/2025/Collegium-Pharmaceutical-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to Moomoo COLL Financials](https://www.moomoo.com/us/stock/COLL/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Scalability is driven by the commercial success of its existing pain portfolio and through the strategic acquisition of other commercial-stage pharmaceutical assets. Growth depends on maintaining market share and expanding its portfolio."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Collegium Pharmaceutical entry updated successfully.")
