
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Hyster-Yale Materials Hndlng":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Hyster-Yale Materials Handling designs, manufactures, and sells a comprehensive line of lift trucks and aftermarket parts, marketed globally primarily under the Hyster and Yale brand names. It also owns Bolzoni, a leader in lift truck attachments. [highlight]Hyster-Yale's competitive moat is built on its strong brand recognition (Hyster and Yale), extensive global distribution network, diversified product portfolio (lift trucks, attachments, hydrogen fuel cell technology), resilience through aftermarket services, commitment to innovation (electrification, automation), and strategic partnerships.[/highlight] [pos]Hyster-Yale Materials Handling has a Return on Invested Capital (ROIC) of 13.78% and a Return on Capital Employed (ROCE) of 0.25% (TipRanks). Its ROIC was 9.07% as of June 2025, with a 5-year average of 3.38%.[/pos] [link to Hyster-Yale Investor Relations](https://www.hyster-yale.com/investors/) [link to TipRanks HY ROIC/ROCE](https://www.tipranks.com/stocks/hy/roic/) [link to Finance Charts HY ROIC](https://financecharts.com/stocks/hy/roic)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]The company is controlled by the founding Rankin family through a dual-class share structure, ensuring a very long-term and stable strategic focus. Insider ownership is approximately 17.13% (Simply Wall St).[/pos] [link to Simply Wall St HY Ownership](https://simplywall.st/stocks/us/industrials/nyse-hy/hyster-yale-materials-handling/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company uses a significant amount of debt to finance its global manufacturing operations, inventory, and leasing portfolio. [pos]As of Q1 2025, Hyster-Yale Materials Handling reported $96.6 million in cash and $440.7 million in debt. The company has an active stock repurchase program, with $50 million or 1.5 million shares authorized until November 2027. In Q4 2024, $5 million of Class A common stock was repurchased. There is no recent information indicating stock dilutions.[/pos] [link to Hyster-Yale Q1 2025 Earnings Release](https://www.hyster-yale.com/news-releases/news-release-details/2025/Hyster-Yale-Materials-Handling-Inc.-Announces-First-Quarter-2025-Results/default.aspx) [link to Stock Titan HY Buybacks](https://stocktitan.net/news/HY/hyster-yale-materials-handling-inc-announces-stock-repurchase-302138033.html)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Scalability is tied to global economic activity and industrial production. Growth comes from gaining market share, expanding its product line (including automation and electric trucks), and growing its high-margin aftermarket parts and service business."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Hyster-Yale Materials Hndlng entry updated successfully.")
