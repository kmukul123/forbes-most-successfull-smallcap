
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Progyny":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Progyny is a benefits management company specializing in fertility and family building solutions for large, self-insured employers. It provides a comprehensive benefits plan that includes access to a network of fertility specialists and integrated pharmacy services. [highlight]Progyny's competitive moat is built on its comprehensive benefits management platform for fertility and family building, its network of high-quality fertility specialists, and its integrated pharmacy services. Its focus on large, self-insured employers and the increasing demand for fertility benefits provide a strong tailwind.[/highlight] [pos]Progyny has a Return on Invested Capital (ROIC) of 19.75% (GuruFocus, TTM as of June 2025) and a Return on Capital Employed (ROCE) of 14.82% (StockAnalysis). Its annualized ROIC for Q1 2025 was 23.33%.[/pos] [link to Progyny Investor Relations](https://investors.progyny.com/) [link to GuruFocus PGNY ROIC](https://www.gurufocus.com/term/roic/NASDAQ:PGNY) [link to StockAnalysis PGNY ROIC/ROCE](https://stockanalysis.com/stocks/pgny/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership varies across sources, from 2.12% (TipRanks) to 40.85% (WallStreetZen), with the latter likely including large institutional holders. Key insider shareholders include Tpg Group Holdings Sbs Advisors Inc and Kleiner Perkins Caufield Byers XIII LLC.[/pos] [link to WallStreetZen PGNY Ownership](https://www.wallstreetzen.com/stocks/us/healthcare/nasdaq-pgny/progyny/ownership) [link to TipRanks PGNY Ownership](https://www.tipranks.com/stocks/pgny/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company is debt-free and has a strong cash position, reflecting its capital-light business model. [pos]As of March 2025, Progyny reported $256.1 million in cash and cash equivalents. Some sources indicate very low total debt (e.g., $25.99 million). Progyny has actively engaged in share buyback programs, with two $100 million programs announced in 2024. In 2024, over 12.3 million shares were repurchased. Its diluted shares outstanding decreased by 11.62% from March 2024 to March 2025, indicating a reduction in shares through buybacks.[/pos] [link to Progyny Q1 2025 Earnings Release](https://investors.progyny.com/news-releases/news-release-details/2025/Progyny-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to Finance Charts PGNY Shares Outstanding](https://financecharts.com/stocks/pgny/shares-outstanding/)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Highly scalable model. Growth is driven by signing up new large employers as clients and by increasing the number of employees (lives) covered under its plans. The increasing demand for fertility benefits as a core part of employee compensation provides a strong tailwind."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Progyny entry updated successfully.")
