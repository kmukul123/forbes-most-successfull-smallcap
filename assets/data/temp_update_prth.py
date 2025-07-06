
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Priority Technology Holdings":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Priority Technology Holdings is a payments technology company that provides integrated payments and banking solutions. It serves various markets, including small businesses, enterprises, and integrated software vendors (ISVs), with its CPX (Collaborative Payments) platform. [highlight]Priority Technology Holdings' competitive moat is built on its integrated payment solutions (one-stop shop), diversified and recurring revenue streams, scalable and innovative technology platform (Priority Commerce Engine), strategic acquisitions, robust distribution network (over 1,100 partners), and focus on SMB and B2B markets.[/highlight] [pos]Priority Technology Holdings has a Return on Capital Employed (ROCE) of 18.00% and a Return on Invested Capital (ROIC) of 11.74% (StockAnalysis).[/pos] [link to Priority Technology Holdings Investor Relations](https://ir.prioritycommerce.com/) [link to StockAnalysis PRTH ROIC/ROCE](https://stockanalysis.com/stocks/prth/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership is very high, with the executive chairman and other key leaders holding a majority of the company, indicating strong alignment and control. Insider ownership is approximately 66.28% (TipRanks) to 75% (Ainvest).[/pos] [link to TipRanks PRTH Ownership](https://www.tipranks.com/stocks/prth/ownership) [link to Ainvest PRTH Ownership](https://ainvest.com/stock/nasdaq/prth/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company has a significant amount of debt on its balance sheet, which was used to finance its platform development and numerous acquisitions. [pos]As of Q4 2024, Priority Technology Holdings reported $58.6 million in unrestricted cash. Gross debt was $945.5 million and net debt was $886.9 million. In May 2024, the company completed a debt refinancing, issuing a new $835 million term loan and establishing a new $70 million revolving line of credit.[/pos] [pos]On June 23, 2025, the Board approved a new $40 million share repurchase program. The adjusted weighted average diluted shares outstanding increased slightly from 78,225 in Q1 2024 to 79,857 in Q1 2025.[/pos] [link to Priority Technology Holdings Q4 2024 Earnings Release](https://ir.prioritycommerce.com/news-releases/news-release-details/2025/Priority-Technology-Holdings-Inc.-Reports-Fourth-Quarter-and-Full-Year-2024-Financial-Results/default.aspx) [link to Priority Technology Holdings Share Repurchase Program](https://ir.prioritycommerce.com/news-releases/news-release-details/2025/Priority-Technology-Holdings-Inc.-Announces-New-Share-Repurchase-Program/default.aspx)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Highly scalable platform-based model. Growth is driven by onboarding more software partners and businesses to its payments platform, which generates recurring, transaction-based revenue. It also scales through strategic acquisitions of payment portfolios."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Priority Technology Holdings entry updated successfully.")
