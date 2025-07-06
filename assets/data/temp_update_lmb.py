
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Limbach Holdings":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Limbach Holdings is a provider of building systems solutions. It specializes in the design, installation, and maintenance of mechanical, electrical, and plumbing (MEP) systems for commercial and institutional buildings. [highlight]Limbach Holdings' competitive moat is built on its strategic shift to Owner Direct Relationships (ODR) for higher-margin recurring revenue, specialized expertise in advanced engineering and technology, quality management systems, strategic acquisitions (e.g., Pioneer Power), and a diversified customer base.[/highlight] [pos]Limbach Holdings has a Return on Invested Capital (ROIC) of 18.76% (GuruFocus, TTM as of July 2025) and a Return on Capital Employed (ROCE) of 19.52% (GuruFocus, annualized as of March 2025). Its ROIC is significantly higher than its WACC (12.63%), indicating value creation.[/pos] [link to Limbach Holdings Investor Relations](https://www.limbachinc.com/investors/) [link to GuruFocus LMB ROIC](https://www.gurufocus.com/term/roic/NASDAQ:LMB) [link to StockAnalysis LMB ROIC/ROCE](https://stockanalysis.com/stocks/lmb/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership is moderate, with GuruFocus reporting 23.49% and TipRanks reporting 9.70%. David S. Gellman is a significant insider shareholder. Insiders have both bought and sold shares recently.[/pos] [link to GuruFocus LMB Ownership](https://www.gurufocus.com/term/insider_ownership/NASDAQ:LMB) [link to TipRanks LMB Ownership](https://www.tipranks.com/stocks/lmb/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company manages a moderate level of debt, often tied to the working capital needs of its large construction projects. [pos]As of March 2025, Limbach Holdings had approximately $38.1 million in cash and short-term investments, with total debt of about $9.6 million, resulting in a net cash position of $28.5 million. Its debt-to-equity ratio has significantly reduced from 78.9% to 6% over the past five years. Debt is well covered by operating cash flow (446%) and interest payments are well covered by EBIT (449.2x coverage).[/pos] [pos]Limbach Holdings has engaged in stock buybacks, including a $2.0 million program in September 2022 and the repurchase of Class A Preferred Stock for $9.974 million in January 2018. Its diluted EPS has shown significant growth (32.89% CAGR over 12 months).[/pos] [link to Limbach Holdings Q1 2025 Earnings Release](https://www.limbachinc.com/news-releases/news-release-details/2025/Limbach-Holdings-Inc.-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to Simply Wall St LMB Financials](https://simplywall.st/stocks/us/industrials/nasdaq-lmb/limbach-holdings/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Scalable by growing its high-margin owner-direct service business, which provides recurring revenue and is less cyclical than new construction. It also scales by acquiring smaller, regional MEP service providers."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Limbach Holdings entry updated successfully.")
