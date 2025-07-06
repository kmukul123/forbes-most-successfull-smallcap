

import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Viant Technology":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Viant Technology is an advertising software company that provides a platform, Adelphic, for advertisers and their agencies to plan, buy, and measure digital advertising campaigns across various channels, including desktop, mobile, and connected TV. [highlight]Viant's competitive moat is built on its people-based advertising approach (cookie-less targeting), superior measurement capabilities, technological and intellectual property advantages, AI-driven solutions (ViantAI, Household ID, Vine.ai), strategic acquisitions (IRIS.TV), and its focus on independent ad tech.[/highlight] [pos]Viant's Return on Capital Employed (ROCE) is 1.55% and Return on Invested Capital (ROIC) is 0.93% (StockAnalysis). GuruFocus reports a ROIC of 3.90% as of May 2025.[/pos] [link to Viant Investor Relations](https://viantinc.com/investor-relations/) [link to StockAnalysis DSP ROIC/ROCE](https://stockanalysis.com/stocks/dsp/roic/) [link to GuruFocus DSP ROIC](https://www.gurufocus.com/term/roic/NASDAQ:DSP)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]The founding brothers and executive team have majority voting control, ensuring a consistent long-term vision for the company's technology and strategy. Insider ownership is approximately 29.40% (MarketBeat), with Timothy and Christopher Vanderhook each holding 31.70%.[/pos] [link to MarketBeat DSP Ownership](https://www.marketbeat.com/stocks/NASDAQ/DSP/institutional-ownership/) [link to WallStreetZen DSP Ownership](https://www.wallstreetzen.com/stocks/us/nasdaq/dsp/viant-technology/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company operates with little to no debt, maintaining a strong cash position to invest in its software platform and sales organization. [pos]As of March 31, 2025, Viant Technology reported $174 million in cash and cash equivalents and no debt. The company has significantly reduced its long-term debt to $0 in recent years.[/pos] [pos]Viant has an active and recently expanded stock repurchase program. In May 2025, the board approved a $50 million increase to the program, with $46.5 million in shares repurchased between May 2024 and May 2025. From January to March 2025, 1,190,314 shares were repurchased for $17.34 million. The company plans to fund these repurchases from existing cash and future cash flows.[/pos] [neg]While there is a focus on buybacks, stock-based compensation can lead to dilution, and \"Shareholder dilution\" was noted as a new minor risk in December 2024.[/neg] [link to Viant Q1 2025 Earnings Release](https://viantinc.com/investor-relations/news-releases/news-release-details/2025/Viant-Technology-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to TipRanks DSP Buybacks](https://www.tipranks.com/stocks/dsp/buybacks)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Highly scalable SaaS model. Growth is driven by the shift of ad dollars to programmatic channels, particularly connected TV. It scales by increasing the number of active customers on its platform and growing the ad spend per customer."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Viant Technology entry updated successfully.")

