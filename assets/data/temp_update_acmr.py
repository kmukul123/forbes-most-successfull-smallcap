
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "ACM Research":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """ACM Research develops, manufactures, and sells single-wafer wet cleaning equipment, which is a critical component in the semiconductor manufacturing process. Its tools are used to improve product yield by removing particles and contaminants from silicon wafers. [highlight]ACM Research's competitive moat is built on its proprietary megasonic technology for wafer cleaning, a comprehensive cleaning tool portfolio covering ~95% of applications, and a dominant position as the leading domestic supplier in China. The company consistently invests heavily in R&D (around 10% of turnover, over 500 patents) and is diversifying its customer base globally.[/highlight] [pos]The company has demonstrated a strong growth trajectory with revenue increasing from $75 million in 2018 to $558 million in 2023 (50% CAGR), and a long-term revenue target of $3 billion.[/pos] [pos]As of March 2025, ACM Research's annualized Return on Invested Capital (ROIC) and Return on Capital Employed (ROCE) were 8.39% (GuruFocus), with TTM figures at 11.36%. Simply Wall St reported a ROCE of 12% as of April 2025, consistent for the last five years. Finance Charts shows a ROIC of 10.10% as of June 2025. While these returns are solid, GuruFocus notes they are below the company's WACC (e.g., 15.52% as of July 2025), suggesting potential value destruction as it grows.[/pos] [neg]A significant portion of ACMR's revenue is generated through its Chinese subsidiary, exposing it to geopolitical risks and potential trade restrictions.[/neg] [link to ACM Research Investor Relations](https://ir.acmrcsh.com/) [link to GuruFocus ACMR ROIC/ROCE](https://www.gurufocus.com/term/roic/NASDAQ:ACMR) [link to Simply Wall St ACMR Financials](https://simplywall.st/stocks/us/semiconductors/nasdaq-acmr/acm-research/financials)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership varies across sources, with TipRanks reporting ~18.39%, Moomoo 13%, GuruFocus 3.4%, and MarketBeat 25%. Simply Wall St indicates insiders hold approximately 12% of the business, valued at ~$190 million, demonstrating strong alignment with shareholder interests.[/pos] [link to TipRanks ACMR Ownership](https://www.tipranks.com/stocks/acmr/ownership) [link to Simply Wall St ACMR Ownership](https://simplywall.st/stocks/us/semiconductors/nasdaq-acmr/acm-research/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company operates with a low level of debt, funding its R&D and expansion primarily through its operational cash flow and equity offerings. [pos]ACM Research maintains a healthy financial position with significant cash and short-term investments, approximately $492.8 million (Simply Wall St) or $467.83 million (BusinessQuant).[/pos] [neg]Total debt is around $227.4 million (Simply Wall St) or $237.14 million (BusinessQuant).[/neg] [pos]The company holds a net cash position, with cash exceeding debt, and a healthy debt-to-equity ratio of 19.7%. Its debt is well covered by operating cash flow (73.6% coverage) and tangible assets (8.14x coverage).[/pos] [neg]However, the number of diluted shares outstanding has generally increased, reaching 67 million as of March 31, 2025 (a 1.52% increase year-over-year), indicating stock dilution rather than significant buyback activity.[/neg] [link to Simply Wall St ACMR Balance Sheet](https://simplywall.st/stocks/us/semiconductors/nasdaq-acmr/acm-research/financials) [link to BusinessQuant ACMR Financials](https://www.businessquant.com/stock/ACMR/financials) [link to GuruFocus ACMR Cash-to-Debt](https://www.gurufocus.com/term/Cash-to-Debt/NASDAQ:ACMR)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Highly scalable, with growth tied to the expansion of the semiconductor industry, particularly in China. It scales by selling more tools to existing customers as they build new fabs and by winning business from new customers with its innovative cleaning technology."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("ACM Research entry updated successfully.")
