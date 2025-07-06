

import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Axogen":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Axogen is a medical technology company focused on developing and marketing surgical solutions for peripheral nerve repair. Its portfolio includes off-the-shelf processed human nerve tissue for grafting, nerve connectors, and nerve protectors. [highlight]Axogen's competitive moat is built on its innovative product offerings (e.g., Avance Nerve Graft), leadership in processed nerve allografts, strong intellectual property (MAPS® processing technology), growing clinical evidence, dedicated sales force, and niche market focus. Analysts anticipate Avance could become the standard of care with potential market exclusivity.[/highlight] [neg]However, Morningstar's quantitative rating for its economic moat is \"None.\"[/neg] [pos]Axogen has a Return on Invested Capital (ROIC) of -0.26% (GuruFocus, as of June 2025) and a Return on Capital Employed (ROCE) of -0.22% (StockAnalysis).[/pos] [link to Axogen Investor Relations](https://www.axogeninc.com/investors/) [link to GuruFocus AXGN ROIC](https://www.gurufocus.com/term/roic/NASDAQ:AXGN) [link to StockAnalysis AXGN ROIC/ROCE](https://stockanalysis.com/stocks/axgn/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership varies across sources, from 2.55% (TipRanks) to 60.49% (WallStreetZen). Matthew T. Moroun is the largest individual shareholder, owning 74.00% of the company. Insiders have both bought and sold shares in the last 24 months.[/pos] [link to WallStreetZen AXGN Ownership](https://www.wallstreetzen.com/stocks/us/medical-devices/nasdaq-axgn/axogen/ownership) [link to TipRanks AXGN Ownership](https://www.tipranks.com/stocks/axgn/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company utilizes a mix of equity and debt to fund its commercialization efforts, clinical studies, and R&D activities. [pos]As of May 8, 2025, Axogen reported $18.096 million in cash and cash equivalents. Total debt was $50.3 million, with long-term debt at $47.716 million. Its net debt to equity ratio is 26.8%, considered satisfactory. The company has a sufficient cash runway for more than three years based on its current free cash flow.[/pos] [link to Axogen Q1 2025 Earnings Release](https://www.axogeninc.com/news-releases/news-release-details/2025/Axogen-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to Simply Wall St AXGN Financials](https://simplywall.st/stocks/us/medical-devices/nasdaq-axgn/axogen/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """High scalability as it is a leader in a niche market with significant unmet needs. Growth is driven by increasing surgeon adoption of its products, expanding the number of active accounts, and developing new products for a broader range of nerve repair procedures."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Axogen entry updated successfully.")

