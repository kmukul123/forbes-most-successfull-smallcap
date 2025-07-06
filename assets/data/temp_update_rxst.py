

import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "RxSight":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """RxSight is a commercial-stage medical technology company that has developed the world's first and only adjustable intraocular lens (IOL). Its Light Adjustable Lens allows ophthalmologists to customize a patient's vision after cataract surgery. [highlight]RxSight's competitive moat is primarily built on its unique and patented Light Adjustable Lens (LAL) technology, which allows post-surgical vision customization. It holds extensive patents (some until 2043), operates on a \"razor-and-blade\" business model, and offers clinical superiority with limited direct competition.[/highlight] [neg]However, potential threats include patent expirations, emerging alternative technologies, and the company's current unprofitability and cash burn.[/neg] [pos]For RxSight, the Return on Invested Capital (ROIC) is -64.88% (GuruFocus, as of June 2025) and the Return on Capital Employed (ROCE) is -12.70% (StockAnalysis).[/pos] [link to RxSight Investor Relations](https://investors.rxsight.com/) [link to GuruFocus RXST ROIC](https://www.gurufocus.com/term/roic/NASDAQ:RXST) [link to StockAnalysis RXST ROIC/ROCE](https://stockanalysis.com/stocks/rxst/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Backed by venture capital and institutional investors. Insider ownership is approximately 9.57% (MarketBeat) or 5.52% (TipRanks).[/pos] [link to MarketBeat RXST Ownership](https://www.marketbeat.com/stocks/NASDAQ/RXST/institutional-ownership/) [link to TipRanks RXST Ownership](https://www.tipranks.com/stocks/rxst/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """Utilizes a mix of equity and debt financing to fund its commercial expansion, R&D, and manufacturing scale-up. [pos]As of September 30, 2024, RxSight reported $237.1 million in cash, cash equivalents, and short-term investments. The company has very low debt, with some sources indicating it is debt-free, while others report total debt of $12.04 million (96% less than its equity).[/pos] [pos]There is no information to suggest significant stock dilutions or buybacks, but the company's focus is on growth and commercialization.[/pos] [link to RxSight Q3 2024 Earnings Release](https://investors.rxsight.com/news-releases/news-release-details/2024/RxSight-Reports-Third-Quarter-2024-Financial-Results/default.aspx) [link to Simply Wall St RXST Financials](https://simplywall.st/stocks/us/medical-devices/nasdaq-rxst/rxsight/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Extremely high scalability. As a first-mover with a disruptive technology, growth is driven by increasing adoption by cataract surgeons. It scales by selling more lenses and the accompanying Light Delivery Devices to ophthalmic practices."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("RxSight entry updated successfully.")
