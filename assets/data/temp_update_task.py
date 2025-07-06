
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "TaskUs":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """TaskUs is a provider of outsourced digital business services, primarily for high-growth technology companies. Its services include digital customer experience, content security, and AI services, helping clients protect and grow their brands. [highlight]TaskUs's competitive moat is built on its integration of high-performing talent and advanced AI (TaskGPT), specialized digital services for high-growth sectors, emphasis on employee wellness and training, customized solutions and strategic client partnerships (Meta, Netflix, Uber), and a first-mover advantage in data labeling.[/highlight] [pos]TaskUs has a Return on Capital Employed (ROCE) of 14.31% and a Return on Invested Capital (ROIC) of 9.33% (StockAnalysis). Its ROCE has substantially increased to 14% over the last five years.[/pos] [link to TaskUs Investor Relations](https://ir.taskus.com/) [link to StockAnalysis TASK ROIC/ROCE](https://stockanalysis.com/stocks/task/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]The co-founders maintain significant ownership and voting control, ensuring a consistent focus on the company's unique culture and strategic direction. Insider ownership is approximately 2.74% (Financhill) to 73.50% (WallStreetZen).[/pos] [link to Financhill TASK Ownership](https://financhill.com/stock/task/insider-ownership) [link to WallStreetZen TASK Ownership](https://www.wallstreetzen.com/stocks/us/commercial-professional-services/nasdaq-task/taskus/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company maintains a healthy balance sheet with a manageable level of debt, providing the flexibility to invest in its global delivery centers and technology. [pos]As of March 31, 2025, TaskUs reported $317.6 million in total cash. Total debt was $646.4 million, resulting in a net debt of -$328.8 million. The company has a current ratio of 3.03. There is no information about stock dilutions or buybacks.[/pos] [link to TaskUs Q1 2025 Earnings Release](https://ir.taskus.com/news-releases/news-release-details/2025/TaskUs-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to Simply Wall St TASK Financials](https://simplywall.st/stocks/us/commercial-professional-services/nasdaq-task/taskus/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Highly scalable model. Growth is driven by the increasing need for specialized outsourcing by fast-growing digital companies. It scales by expanding its service lines with existing clients ('land and expand') and by winning new clients in disruptive industries."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("TaskUs entry updated successfully.")
