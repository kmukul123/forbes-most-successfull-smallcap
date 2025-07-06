
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Energy Recovery":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Energy Recovery, Inc. designs and manufactures energy recovery devices for the water and industrial fluid-flow markets. Its core technology, the Pressure Exchanger, significantly reduces energy consumption in seawater reverse osmosis (desalination) plants. [highlight]Energy Recovery's competitive moat is built on its proprietary Pressure Exchanger technology, which is a market leader in desalination and has high barriers to entry. The company is expanding into new industrial markets like CO2 refrigeration, leveraging its core technology. Its strong financial position with no debt provides flexibility for growth.[/highlight] [pos]Energy Recovery has a Return on Capital Employed (ROCE) of 10% (Simply Wall St, as of December 2024) and a Return on Invested Capital (ROIC) of 6.02% (StockAnalysis). Its 5-year average ROIC was 24.5%.[/pos] [link to Energy Recovery Investor Relations](https://ir.energyrecovery.com/) [link to Simply Wall St ERII ROCE](https://simplywall.st/stocks/us/industrials/nasdaq-erii/energy-recovery/financials) [link to StockAnalysis ERII ROIC](https://stockanalysis.com/stocks/erii/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership is moderate, with TipRanks reporting 2.87% and Simply Wall St indicating 2.1%. Insiders have both bought and sold shares recently.[/pos] [link to TipRanks ERII Ownership](https://www.tipranks.com/stocks/erii/ownership) [link to Simply Wall St ERII Ownership](https://simplywall.st/stocks/us/industrials/nasdaq-erii/energy-recovery/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company is debt-free and holds a large cash balance, which it is using to fund its expansion into new industrial markets like CO2 refrigeration. [pos]Energy Recovery has consistently maintained a debt-free status ($0.0 total debt) for at least the past five years. As of March 2025, it held $83.5 million in cash and short-term investments.[/pos] [pos]Energy Recovery has actively engaged in share repurchase programs. A new $30 million program began in February 2025, following the completion of a $50 million program in November 2024, under which 3.2 million shares were repurchased. Over a five-year period, the company has reduced its share count by 2.9% through buybacks, contributing to EPS growth. As of June 2025, 54,499,225 shares were outstanding.[/pos] [link to Energy Recovery Q1 2025 Earnings Release](https://ir.energyrecovery.com/news-releases/news-release-details/2025/Energy-Recovery-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to Simply Wall St ERII Financials](https://simplywall.st/stocks/us/industrials/nasdaq-erii/energy-recovery/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Very high scalability potential. While dominant in desalination, its primary growth vector is adapting its pressure exchanger technology for new, large industrial applications. A successful entry into the CO2 refrigeration market would dramatically scale the business."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Energy Recovery entry updated successfully.")
