
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Barrett Business Services":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Barrett Business Services, Inc. (BBSI) is a leading provider of business management solutions, combining human resource outsourcing (PEO) and staffing services. It helps small and mid-sized businesses by managing payroll, benefits, and workers' compensation. [highlight]BBSI's competitive moat is built on its integrated service model (PEO and staffing), deep expertise in workers' compensation risk management, local presence with strong referral networks, niche market focus on SMBs, and an asset-light growth model.[/highlight] [pos]Barrett Business Services has a Return on Invested Capital (ROIC) of 16.83% and a Return on Capital Employed (ROCE) of 17.70% (StockAnalysis). Its returns on capital have increased by 57% over the trailing five years.[/pos] [link to BBSI Investor Relations](https://www.bbsi.com/investor-relations) [link to StockAnalysis BBSI ROIC/ROCE](https://stockanalysis.com/stocks/bbsi/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership is significant, with 19.52% (WallStreetZen) of the company owned by insiders. William W. Sherertz (10.00%) and Nancy B. Sherertz (4.38%) are key insider shareholders.[/pos] [link to WallStreetZen BBSI Ownership](https://www.wallstreetzen.com/stocks/us/commercial-professional-services/nasdaq-bbsi/barrett-business-services/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company maintains a strong, debt-free balance sheet, which is a key advantage in managing its workers' compensation insurance risk. [pos]As of March 31, 2025, cash and cash equivalents were $55.367 million. The company was debt-free at the end of 2024. In Q4 2024, BBSI repurchased $7 million of its stock (162,100 shares). Approximately $29.8 million remained available under its $75 million stock repurchase program. The total number of shares outstanding decreased by 2.65% over one year.[/pos] [link to BBSI Q1 2025 Earnings Release](https://www.bbsi.com/news-releases/news-release-details/2025/Barrett-Business-Services-Inc.-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to StockAnalysis BBSI Financials](https://stockanalysis.com/stocks/bbsi/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Scalable model focused on organic growth. It scales by adding new clients through its branch network and by increasing the number of worksite employees it manages. Its integrated PEO and staffing model provides a strong competitive advantage."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Barrett Business Services entry updated successfully.")
