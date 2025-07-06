
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Bioventus":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Bioventus is a medical device company focused on developing and commercializing clinically differentiated, cost-effective solutions that engage and enhance the body's natural healing process. Its products focus on pain treatment, restorative therapies, and surgical solutions. [highlight]Bioventus's competitive moat is built on its proprietary technology and patents (82 active patents in 2022), specialized focus in orthobiologics and regenerative medicine, established distribution network, brand reputation, innovative product portfolio (e.g., Exogen, Stimrouter), and strategic acquisitions. It emphasizes minimally invasive procedures.[/highlight] [pos]Bioventus has a Return on Invested Capital (ROIC) of -0.26% and a Return on Capital Employed (ROCE) of -0.22% (StockAnalysis).[/pos] [link to Bioventus Investor Relations](https://www.bioventus.com/investors/) [link to StockAnalysis BVS ROIC/ROCE](https://stockanalysis.com/stocks/bvs/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Primarily owned by institutional investors. Insider ownership is approximately 6.96% (GuruFocus).[/pos] [link to GuruFocus BVS Ownership](https://www.gurufocus.com/term/insider_ownership/NASDAQ:BVS)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company has a highly leveraged balance sheet with a substantial amount of debt resulting from its history of large, strategic acquisitions. [pos]As of March 28, 2025, Bioventus reported approximately $22.8 million in cash and short-term investments, with total debt of around $345.9 million. Its debt-to-equity ratio was 186.5%.[/pos] [link to Simply Wall St BVS Financials](https://simplywall.st/stocks/us/medical-devices/nasdaq-bvs/bioventus/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Scalable through its broad portfolio of products and a large, direct sales force. Growth comes from increasing market penetration of its existing products, launching new products, and acquiring complementary technologies or businesses."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Bioventus entry updated successfully.")
