
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Tutor Perini":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Tutor Perini Corporation is a leading civil, building, and specialty construction company. It undertakes large, complex public and private infrastructure projects, such as bridges, tunnels, airports, and high-rise buildings. [highlight]Tutor Perini's competitive moat is built on its extensive experience and strong reputation in executing large, complex projects, vertical integration (specialized services), focus on large and complex projects (high barriers to entry), and significant public sector/government contracts. It benefits from a substantial project backlog ($19.4 billion by March 2025) and specialized technical capabilities.[/highlight] [neg]However, some analyses suggest it lacks a strong economic moat due to low switching costs and limited brand power.[/neg] [pos]Tutor Perini has a Return on Capital Employed (ROCE) of -4.69% and a Return on Invested Capital (ROIC) of -2.81% (StockAnalysis). Its ROIC was 7.12% for the quarter ending March 2025.[/pos] [link to Tutor Perini Investor Relations](https://www.tutorperini.com/investor-relations) [link to StockAnalysis TPC ROIC/ROCE](https://stockanalysis.com/stocks/tpc/roic/) [link to GuruFocus TPC ROIC](https://www.gurufocus.com/term/roic/NYSE:TPC)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]The CEO holds a very large and influential stake in the company, demonstrating a powerful commitment to its operational success. Insider ownership is approximately 15.93% (TipRanks) to 82.16% (WallStreetZen), with Ronald N. Tutor owning 44.15%.[/pos] [link to TipRanks TPC Ownership](https://www.tipranks.com/stocks/tpc/ownership) [link to WallStreetZen TPC Ownership](https://www.wallstreetzen.com/stocks/us/industrials/nyse-tpc/tutor-perini/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company operates with a significant amount of debt and relies on surety bonds to undertake its large-scale construction projects. [pos]As of December 2024, Tutor Perini reported $455.1 million in cash, with total debt of $534.1 million, resulting in a net debt of $79.1 million. The company has significantly reduced its debt by $477 million (52%) since December 2023. It anticipates continued strong operating cash flow to further strengthen its balance sheet.[/pos] [pos]Tutor Perini has engaged in share buyback programs in the past, with a $100 million program announced in March 2010. The company did not repurchase any common stock in Q4 2024. Diluted EPS was $0.53 in Q1 2025, a 77% increase year-over-year.[/pos] [link to Tutor Perini Q1 2025 Earnings Release](https://www.tutorperini.com/news-releases/news-release-details/2025/Tutor-Perini-Reports-First-Quarter-2025-Results/default.aspx) [link to Simply Wall St TPC Financials](https://simplywall.st/stocks/us/industrials/nyse-tpc/tutor-perini/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Scalability is project-based and depends on its ability to win large, multi-billion dollar contracts. Growth is driven by increased government infrastructure spending. The company's scale and expertise in complex projects provide a competitive advantage."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Tutor Perini entry updated successfully.")
