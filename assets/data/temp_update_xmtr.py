
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Xometry":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Xometry operates a global AI-driven marketplace for on-demand manufacturing. It connects enterprise buyers with a network of suppliers for services like 3D printing, CNC machining, injection molding, and sheet metal fabrication. [highlight]Xometry's competitive moat is built on its AI-powered marketplace (instant quotes, optimized matching), strong network effects (more buyers/suppliers increase value), data-driven insights, early-mover advantage, high customer retention, and broad service offerings.[/highlight] [pos]Xometry has a Return on Invested Capital (ROIC) of -14.01% (GuruFocus, TTM as of July 2025) and a Return on Capital Employed (ROCE) of -8.66% (StockAnalysis). Its ROIC has shown an increasing trend, moving from -32% to -13%.[/pos] [link to Xometry Investor Relations](https://investors.xometry.com/) [link to GuruFocus XMTR ROIC](https://www.gurufocus.com/term/roic/NASDAQ:XMTR) [link to StockAnalysis XMTR ROIC/ROCE](https://stockanalysis.com/stocks/xmtr/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Founders, executives, and early-stage investors hold stakes, but the majority of shares are held by institutional investors. Insider ownership is approximately 9.66% (TipRanks) to 9.82% (MarketBeat).[/pos] [link to TipRanks XMTR Ownership](https://www.tipranks.com/stocks/xmtr/ownership) [link to MarketBeat XMTR Ownership](https://www.marketbeat.com/stocks/NASDAQ/XMTR/institutional-ownership/)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """Maintains a strong balance sheet with a healthy cash position and minimal debt, allowing for investment in its platform and potential acquisitions. [pos]As of March 30, 2025, Xometry reported $231.4 million in cash and short-term investments. Total debt was approximately $284.1 million, with a net debt of approximately $49.1 million as of September 2024. The company has a stable cash runway for more than three years based on its current free cash flow.[/pos] [neg]The debt-to-equity ratio increased to 91.3% as of March 2025 from 25.8% over the past five years.[/neg] [link to Simply Wall St XMTR Financials](https://simplywall.st/stocks/us/industrials/nasdaq-xmtr/xometry/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Extremely scalable marketplace model. Growth is driven by network effects: more buyers attract more suppliers, which in turn expands capabilities and attracts more buyers. It scales by expanding its service offerings, geographic reach, and software tools for both sides of the marketplace."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Xometry entry updated successfully.")
