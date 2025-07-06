
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Riley Exploration Permian":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Riley Exploration Permian is an independent oil and natural gas company focused on the acquisition and development of assets in the Permian Basin, one of the most prolific oil-producing regions in the United States. [highlight]Its competitive moat is primarily derived from its strategic focus on the Permian Basin, a highly prolific and cost-effective oil and gas producing region, and its operational efficiency in developing these assets.[/highlight] [pos]Riley Exploration Permian has a Return on Invested Capital (ROIC) of 13.26% and a Return on Capital Employed (ROCE) of 18.95% (StockAnalysis). Its ROIC has shown growth, increasing by 8% from the previous quarter.[/pos] [link to Riley Exploration Permian Investor Relations](https://rileypermian.com/investors/) [link to StockAnalysis REPX ROIC/ROCE](https://stockanalysis.com/stocks/repx/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership is significant, with the management team and related parties holding a large stake, aligning them with shareholder value creation. Insider ownership varies across sources, from 4.70% (MarketBeat) to 33.60% (TipRanks).[/pos] [link to TipRanks REPX Ownership](https://www.tipranks.com/stocks/repx/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company uses a revolving credit facility to fund its drilling and development activities but maintains a manageable leverage ratio, balancing growth with financial prudence. [pos]As of March 31, 2025, the company's total debt stood at $259 million (comprising $99 million in borrowings on its Credit Facility and $160 million in Senior Notes), with $9 million in cash. REPX has been actively reducing its debt, with a $90 million reduction in 2024 and a $21 million reduction in Q1 2025. Its debt-to-equity ratio was 0.47 (Simply Wall St).[/pos] [link to Riley Exploration Permian Q1 2025 Earnings Release](https://www.prnewswire.com/news-releases/riley-exploration-permian-inc-announces-first-quarter-2025-financial-and-operating-results-302138033.html) [link to Simply Wall St REPX Financials](https://simplywall.st/stocks/us/energy/nasdaq-repx/riley-exploration-permian/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Scalability is tied to the price of oil and the successful execution of its drilling program. Growth comes from developing its inventory of drilling locations, optimizing production techniques, and potentially acquiring adjacent acreage."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Riley Exploration Permian entry updated successfully.")
