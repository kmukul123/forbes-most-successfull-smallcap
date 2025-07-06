
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "SkyWater Technology":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """SkyWater Technology is a U.S.-based, pure-play semiconductor foundry. It provides manufacturing and process development services for a wide range of customers in markets like aerospace and defense, automotive, and medical. [highlight]SkyWater Technology's competitive moat is built on its strategic scarcity (DMEA Cat-1A accreditation, U.S. controlled IP), Technology as a Service (TaaS) model (customer-funded co-development), niche market focus (specialized, high-value production), and expertise in proprietary IP. The acquisition of Fab 25 further enhances its domestic capacity.[/highlight] [pos]SkyWater Technology has a Return on Capital Employed (ROCE) of 3.3% as of March 2025, showing an upward trend over the last five years. Its current Return on Invested Capital (ROIC) is 1.9%.[/pos] [link to SkyWater Technology Investor Relations](https://ir.skywatertechnology.com/) [link to Simply Wall St SKYT ROCE](https://simplywall.st/stocks/us/semiconductors/nasdaq-skyt/skywater-technology/financials) [link to Value Sense SKYT ROIC](https://valuesense.io/stocks/SKYT/roic)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership is significant, with 37.85% (MarketBeat) to 19.59% (GuruFocus) of the company owned by insiders. Loren A. Unterseher is the largest individual shareholder. Insiders have sold a significant number of shares in the last 24 months.[/pos] [link to MarketBeat SKYT Ownership](https://www.marketbeat.com/stocks/NASDAQ/SKYT/institutional-ownership/) [link to GuruFocus SKYT Ownership](https://www.gurufocus.com/term/insider_ownership/NASDAQ:SKYT)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company utilizes debt and government funding (e.g., from the CHIPS Act) to finance the expansion and upgrading of its foundry capabilities. [pos]As of March 29, 2025, SkyWater Technology had $51.2 million in cash and short-term investments, with total debt of $60.2 million. As of December 2024, net debt was approximately $20.6 million. The company has consistently maintained a debt-free status ($0.0 total debt) for at least the past five years. As of March 2025, it held $83.5 million in cash and short-term investments.[/pos] [neg]SkyWater Technology has experienced stock dilution, with shares outstanding increasing by 2.68% over the past year to approximately 48.04 million shares. Stockholders approved an increase of 4.222 million shares for the 2021 Equity Incentive Plan and 750,000 shares for the 2021 Employee Stock Purchase Plan. The company does not have a history of share buyback programs and does not pay cash dividends.[/neg] [link to Simply Wall St SKYT Financials](https://simplywall.st/stocks/us/semiconductors/nasdaq-skyt/skywater-technology/financials) [link to StockAnalysis SKYT Shares Outstanding](https://stockanalysis.com/stocks/skyt/shares-outstanding/)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Scalable by increasing the utilization of its foundry and by securing government and commercial contracts for advanced semiconductor manufacturing. As the only U.S.-owned pure-play foundry, it is well-positioned to benefit from onshoring trends."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("SkyWater Technology entry updated successfully.")
