
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "NOW":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """NOW Inc., operating as DistributionNOW, is a global distributor of energy and industrial products. It supplies a wide range of equipment, MRO supplies, and solutions to the upstream, midstream, and downstream energy sectors, as well as other industries. [highlight]NOW Inc.'s competitive moat is built on its extensive product portfolio, global footprint (165 locations across 80 countries), strong relationships with manufacturers and customers, supply chain expertise, digital transformation initiatives (DigitalNOW®), and strong financial position with no long-term debt. It also benefits from strategic acquisitions and a diversified customer base.[/highlight] [pos]NOW Inc. has a Return on Invested Capital (ROIC) of 8.60% (GuruFocus, as of April 2025). Its annualized ROIC for Q4 2024 was 9.14%.[/pos] [link to NOW Inc. Investor Relations](https://ir.dnow.com/) [link to GuruFocus DNOW ROIC](https://www.gurufocus.com/term/roic/NYSE:DNOW)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership is modest, with Stock Titan reporting 2.28% and TipRanks reporting 2.35%. Insider holdings have slightly decreased from 2.16% to 2.10% in June 2025.[/pos] [link to Stock Titan DNOW Ownership](https://stocktitan.net/news/DNOW/now-inc-insider-trades-dnow-stock-titan-2-28-insider-ownership-as-of-july-1-2025.html) [link to TipRanks DNOW Ownership](https://www.tipranks.com/stocks/dnow/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """Maintains a strong, low-debt balance sheet, which provides the flexibility to navigate the cyclical nature of the energy industry. [pos]As of December 31, 2024, NOW Inc. reported $256 million in cash and cash equivalents, with zero long-term debt. This trend of being debt-free extends back at least five years. The company has actively engaged in share buyback programs, with a new $160 million program announced in January 2025. As of July 2025, shares outstanding stood at 106 million, a 0.43% decrease over the past year, indicating a reduction in shares through buybacks.[/pos] [link to NOW Inc. Q4 2024 Earnings Release](https://ir.dnow.com/news-releases/news-release-details/2025/NOW-Inc.-Announces-Fourth-Quarter-and-Full-Year-2024-Results/default.aspx) [link to NOW Inc. Share Repurchase Program](https://ir.dnow.com/news-releases/news-release-details/2025/NOW-Inc.-Announces-New-Share-Repurchase-Program/default.aspx)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Scalability is tied to the capital spending of its energy and industrial customers. It can scale by gaining market share, expanding its digital commerce platform (DigitalNOW), and making strategic acquisitions of smaller distributors."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("NOW entry updated successfully.")
