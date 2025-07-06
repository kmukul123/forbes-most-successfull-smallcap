
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Hovnanian Enterprises":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Hovnanian Enterprises is a national homebuilder in the United States. The company designs, constructs, markets, and sells a variety of residential homes, including single-family homes, townhomes, and condominiums, across multiple states. [neg]Hovnanian operates in a highly competitive homebuilding industry with no explicit strong competitive moat, competing on factors like reputation, price, location, design, quality, service, and amenities.[/neg] [pos]As of TTM, Hovnanian's Return on Capital Employed (ROCE) is 10.40% and Return on Invested Capital (ROIC) is 7.30%.[/pos] [link to StockAnalysis HOV ROIC/ROCE](https://stockanalysis.com/stocks/hov/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]The founding Hovnanian family, including the CEO, maintains significant control and ownership of the company, guiding its long-term strategy. Insider ownership is approximately 10.56% (TipRanks) to 19.77% (MarketBeat).[/pos] [neg]However, insiders have been selling company stock in the last 24 months.[/neg] [link to TipRanks HOV Ownership](https://www.tipranks.com/stocks/hov/ownership) [link to MarketBeat HOV Insider Trading](https://www.marketbeat.com/stocks/NYSE/HOV/insider-trades/)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company has historically operated with a high level of debt, a common feature in the capital-intensive homebuilding industry. It is actively focused on deleveraging and improving its balance sheet. [pos]As of October 31, 2024, cash and cash equivalents were approximately $210.0 million.[/pos] [neg]Total debt is reported around $1.0 billion to $1.12 billion, with S&P Global Ratings forecasting $1.2 billion to $1.3 billion for the foreseeable future. Net debt was approximately $1.01 billion as of April 2023. Operating cash flow is negative, suggesting debt is not well covered, though S&P upgraded its rating due to improved debt leverage (debt to EBITDA of 3.2x as of April 2024).[/neg] [pos]The number of shares outstanding decreased by 2.65% in one year, and shareholders have not been meaningfully diluted in the past year.[/pos] [link to Hovnanian Q4 2024 Earnings Release](https://www.gcs-web.com/hovnanian-enterprises-inc/news-releases/news-release-details/2024/Hovnanian-Enterprises-Inc.-Reports-Fourth-Quarter-and-Fiscal-2024-Results/default.aspx) [link to Simply Wall St HOV Financials](https://simplywall.st/stocks/us/consumer-durables/nyse-hov/hovnanian-enterprises/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Scalability is cyclical and depends on the health of the U.S. housing market, including interest rates and consumer demand. Growth is achieved by acquiring and developing land in desirable locations and managing construction costs effectively."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Hovnanian Enterprises entry updated successfully.")
