
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Karat Packaging":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Karat Packaging is a manufacturer and distributor of single-use, disposable foodservice products, such as food and take-out containers, cups, and utensils. It serves a wide range of restaurants and foodservice operators, with a focus on environmentally friendly options. [pos]Karat Packaging has a Return on Capital Employed (ROCE) of 15.17% and a Return on Invested Capital (ROIC) of 14.03% (GuruFocus, TTM as of June 2025). Its average annual ROIC has been 13.3% over the past three years and 14.8% over the past five years.[/pos] [link to Karat Packaging Investor Relations](https://karatpackaging.com/investors/) [link to GuruFocus KRT ROIC](https://www.gurufocus.com/term/roic/NASDAQ:KRT) [link to StockAnalysis KRT ROIC/ROCE](https://stockanalysis.com/stocks/krt/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]The founders and CEO own a majority of the company, ensuring strong, centralized control and a deep understanding of the business. Insider ownership varies across sources, from 44.00% (MarketBeat) to 91.69% (WallStreetZen). Marvin Cheng (60.42%) and Alan Yu (30.93%) are significant insider shareholders.[/pos] [link to WallStreetZen KRT Ownership](https://www.wallstreetzen.com/stocks/us/consumer-defensive/nasdaq-krt/karat-packaging/ownership) [link to TipRanks KRT Ownership](https://www.tipranks.com/stocks/krt/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company uses a moderate amount of debt to finance its inventory, distribution centers, and manufacturing facilities. [pos]Karat Packaging reported $56.27 million in cash and $100.71 million in total debt. The company has experienced stock dilution through secondary offerings by its management (e.g., 1.5 million shares in June 2025), where the company itself did not receive proceeds. There is no information about stock buybacks.[/pos] [link to Forbes KRT Financials](https://www.forbes.com/companies/karat-packaging/) [link to StockAnalysis KRT Financials](https://stockanalysis.com/stocks/krt/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Scalable by expanding its distribution network, increasing its U.S.-based manufacturing to reduce reliance on imports, and growing its portfolio of eco-friendly products. The fragmented nature of the market also offers acquisition opportunities."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Karat Packaging entry updated successfully.")
