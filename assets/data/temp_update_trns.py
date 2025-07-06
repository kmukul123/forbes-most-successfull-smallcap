
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Transcat":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Transcat is a leading provider of accredited calibration and compliance services. It also distributes professional-grade handheld test, measurement, and control instrumentation. Its services are critical for regulated industries like life sciences and aerospace. [highlight]Transcat's competitive moat is built on its specialized accredited services (ISO/IEC 17025), comprehensive one-stop solution (calibration and distribution), extensive geographic network (29 service centers), strong industry expertise and reputation, recurring revenue from service agreements, and strategic acquisitions. Its focus on highly regulated markets creates high switching costs.[/highlight] [pos]Transcat has a Return on Capital Employed (ROCE) of 5.22% and a Return on Invested Capital (ROIC) of 3.87% (StockAnalysis). Its ROCE has decreased from 10% over the last five years, indicating that while capital is being utilized, it may take time for investments to yield higher returns.[/pos] [link to Transcat Investor Relations](https://www.transcat.com/investor-relations) [link to StockAnalysis TRNS ROIC/ROCE](https://stockanalysis.com/stocks/trns/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership is moderate, with 10.53% of the stock owned by insiders (Financhill). The management team's interests are aligned with performance through stock ownership and incentive plans. Insiders have bought more shares than they have sold in the last three months.[/pos] [link to Financhill TRNS Ownership](https://financhill.com/stock/trns/insider-ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company uses debt strategically to fund its primary growth driver: the acquisition of smaller calibration labs. [pos]As of March 29, 2025, Transcat had $4.64 million in cash and $32.7 million in total debt. Its net debt to equity ratio is 10.9%, a significant reduction from 42.7% over the past five years. Debt is well covered by operating cash flow (119.2% coverage) and interest payments are well covered by EBIT (6x coverage).[/pos] [link to Transcat Q4 2025 Earnings Release](https://www.transcat.com/news-releases/news-release-details/2025/Transcat-Reports-Fourth-Quarter-and-Fiscal-Year-2025-Results/default.aspx) [link to Simply Wall St TRNS Financials](https://simplywall.st/stocks/us/capital-goods/nasdaq-trns/transcat/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Highly scalable business model focused on a 'buy and build' strategy. It acquires small, independent calibration labs and integrates them into its national network, creating operational efficiencies and cross-selling opportunities in a fragmented market."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Transcat entry updated successfully.")
