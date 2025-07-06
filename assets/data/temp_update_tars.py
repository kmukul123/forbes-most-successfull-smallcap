
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Tarsus Pharmaceuticals":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Tarsus Pharmaceuticals is a commercial-stage biopharmaceutical company focused on the treatment of ophthalmic conditions. Its lead product, XDEMVY, is the first and only FDA-approved treatment for Demodex blepharitis, a common eyelid disease. [highlight]Tarsus Pharmaceuticals' competitive moat is built on patent protection and unique formulation of XDEMVY, its first-mover advantage as the only FDA-approved treatment for Demodex blepharitis, and its focus on targeted treatments for underserved conditions. It also benefits from strong clinical data and intellectual property.[/highlight] [pos]Tarsus Pharmaceuticals has a Return on Invested Capital (ROIC) of -18.90% (TarsusRx).[/pos] [link to Tarsus Pharmaceuticals Investor Relations](https://ir.tarsusrx.com/) [link to TarsusRx TARS ROIC](https://tarsusrx.com/investors/financial-information/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Backed by major venture capital and institutional biotech investors. Insider ownership is approximately 3.32% (Fintel) to 8.00% (MarketBeat).[/pos] [link to MarketBeat TARS Ownership](https://www.marketbeat.com/stocks/NASDAQ/TARS/institutional-ownership/) [link to Fintel TARS Ownership](https://fintel.io/n/us/tars)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company has utilized a mix of equity and debt financing to fund the clinical development and successful commercial launch of its lead product. [pos]As of March 31, 2025, Tarsus Pharmaceuticals reported $407.92 million in cash and cash equivalents, with total debt of $72.37 million, resulting in a net cash position of $335.55 million.[/pos] [neg]Tarsus Pharmaceuticals has primarily engaged in stock dilutions through public offerings (e.g., $125.0 million offering in March 2025), leading to a consistent increase in shares outstanding (e.g., 39.345 million shares in June 2025). There is no information about stock buybacks.[/neg] [link to Tarsus Pharmaceuticals Q1 2025 Earnings Release](https://ir.tarsusrx.com/news-releases/news-release-details/2025/Tarsus-Pharmaceuticals-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to CompaniesMarketCap TARS Shares Outstanding](https://companiesmarketcap.com/tarsus-pharmaceuticals/shares-outstanding/)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Very high scalability. As the first-to-market treatment for a widespread condition, growth is driven by physician and patient education and securing broad reimbursement. Its pipeline includes other potential applications for its lead molecule, which could further scale the business."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Tarsus Pharmaceuticals entry updated successfully.")
