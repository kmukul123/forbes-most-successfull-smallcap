
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "DXP Enterprises":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """DXP Enterprises is a leading products and service distributor for MRO (maintenance, repair, and operating) and OEM (original equipment manufacturer) customers. It provides rotating equipment, bearings, power transmission, and industrial supplies. [pos]DXP Enterprises has a Return on Capital Employed (ROCE) of 13.95% and a Return on Invested Capital (ROIC) of 9.49% (StockAnalysis). Its ROCE has risen substantially to 13% over the last five years, and its average ROIC over 5 years is 6.71%.[/pos] [link to DXP Enterprises Investor Relations](https://www.dxpe.com/investor-relations/) [link to StockAnalysis DXPE ROIC/ROCE](https://stockanalysis.com/stocks/dxpe/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]The Chairman and CEO holds a significant stake in the company, ensuring strong, consistent leadership and an owner-operator mindset. Insider ownership is approximately 18.37% (TipRanks) to 19.99% (GuruFocus).[/pos] [link to TipRanks DXPE Ownership](https://www.tipranks.com/stocks/dxpe/ownership) [link to GuruFocus DXPE Ownership](https://www.gurufocus.com/term/insider_ownership/NASDAQ:DXPE)"""

        # Update balancesheet with cash levels and debt details
        company["DESCRIPTION"]["balancesheet"] = """The company uses a considerable amount of debt to finance its inventory and its active acquisition strategy in the fragmented industrial distribution market. [pos]As of March 31, 2025, DXP Enterprises reported $114.3 million in cash on its balance sheet. Total debt outstanding was $647.3 million. As of Q4 2024, gross debt was $945.5 million and net debt was $886.9 million. The company completed a debt refinancing in May 2024, issuing a new $835 million term loan and establishing a new $70 million revolving line of credit.[/pos] [link to DXP Enterprises Q1 2025 Earnings Release](https://www.dxpe.com/news-releases/news-release-details/2025/DXP-Enterprises-Inc.-Announces-First-Quarter-2025-Financial-Results/default.aspx) [link to Simply Wall St DXPE Financials](https://simplywall.st/stocks/us/industrials/nasdaq-dxpe/dxp-enterprises/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Highly scalable through its proven 'buy and build' strategy. DXP acquires smaller regional distributors and integrates them into its platform, creating synergies and expanding its geographic and end-market reach."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("DXP Enterprises entry updated successfully.")
