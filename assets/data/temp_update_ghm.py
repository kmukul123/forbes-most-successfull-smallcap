

import json

file_path = "D:\\users\\mukul\\SharedMukul\\Src\\forbes\\forbes-angular\\src\\assets\\data\\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Graham":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information
        company["DESCRIPTION"]["overview"] = """Graham Corporation designs and manufactures mission-critical equipment for the defense, space, energy, and chemical processing industries. Its products include vacuum systems, heat exchangers, and power generation components. [highlight]Graham's competitive moat is built on its specialized engineering expertise (37 active patents), high product reliability (99.7%), strong customer relationships, and critical role in industries with high switching costs like defense.[/highlight] [link to Graham Corp Investor Relations](https://www.grahamcorp.com/investor-relations)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership is modest, with TipRanks reporting approximately 5.98% as of July 2025, and Trendlyne reporting 6.51% in March 2025.[/pos] [link to TipRanks GHM Ownership](https://www.tipranks.com/stocks/ghm/ownership) [link to Trendlyne GHM Insider Trading](https://trendlyne.com/equity/share-holding/1400/GHM/latest/graham-corp/)"""

        # Update balancesheet with cash levels and debt details
        company["DESCRIPTION"]["balancesheet"] = """[pos]As of March 31, 2025, the company reported $21.6 million in cash and cash equivalents and no debt outstanding.[/pos] This strong balance sheet provides the financial stability needed to bid on large, long-cycle government and industrial projects. [link to Graham Corp Q4 2025 Earnings Release](https://www.grahamcorp.com/news-releases/news-release-details/2025/Graham-Corporation-Announces-Fourth-Quarter-and-Fiscal-Year-2025-Financial-Results/default.aspx)"""

        # Update stock dilutions/buybacks
        company["DESCRIPTION"]["stock_dilutions_buybacks"] = """[pos]Graham has a history of stock buybacks, with varying amounts repurchased quarterly. The company completed a $9.45 million repurchase of 539,000 shares as of March 31, 2025, and has an authorized stock repurchase program of up to $18 million.[/pos] [link to TipRanks GHM Buybacks](https://www.tipranks.com/stocks/ghm/buybacks) [link to MarketScreener GHM News](https://www.marketscreener.com/quote/stock/GRAHAM-CORPORATION-12500/news/Graham-Corporation-Announces-Fourth-Quarter-and-Fiscal-Year-2025-Financial-Results-40000000/)"""

        # Update ROCE/ROIC
        company["DESCRIPTION"]["roic_roce"] = """[pos]Graham Corporation has a reported Return on Invested Capital (ROIC) of 11.11% (Normalized). Over the last five years, the company's average ROIC was 4.2%, showing an increasing trend. The company aims for projects with an expected ROIC of over 20%.[/pos] [link to Morningstar GHM ROIC](https://www.morningstar.com/stocks/xnys/ghm/quote/valuation) [link to Graham Corp Investor Presentation](https://www.grahamcorp.com/investor-relations/presentations)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Scalable, with significant growth opportunities in the defense and space sectors, particularly with the U.S. Navy. It scales by winning large, multi-year contracts and through strategic acquisitions of specialized engineering firms."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Graham entry updated successfully.")
