import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Ocular Therapeutix":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Ocular Therapeutix is a biopharmaceutical company focused on the development and commercialization of therapies for diseases and conditions of the eye. Its proprietary hydrogel platform technology is used to create sustained-release drug delivery products. [highlight]Ocular Therapeutix's competitive moat is built on its proprietary ELUTYX bioresorbable hydrogel platform technology for sustained drug delivery, extensive intellectual property portfolio (87 issued patents), and flagship product DEXTENZA. Its robust pipeline, particularly AXPAXLI for wet AMD, has blockbuster potential due to its long-acting effect and ability to address unmet medical needs.[/highlight] [neg]However, Morningstar assigns \"Economic Moat: None.\"[/neg] [pos]Ocular Therapeutix has a Return on Invested Capital (ROIC) of -31.18% and a Return on Capital Employed (ROCE) of -55.89% (StockAnalysis). Its ROIC was -199.83% as of June 2025, with a 3-year average of -106.53%.[/pos] [link to Ocular Therapeutix Investor Relations](https://investors.ocutx.com/) [link to StockAnalysis OCUL ROIC/ROCE](https://stockanalysis.com/stocks/ocul/roic/) [link to Finance Charts OCUL ROIC](https://financecharts.com/stocks/ocul/roic)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Backed by major biotech institutional investors. Insider ownership is approximately 1.17% (TipRanks).[/pos] [link to TipRanks OCUL Ownership](https://www.tipranks.com/stocks/ocul/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company utilizes a mix of royalty income, equity financing, and debt to fund its commercial products and its extensive clinical pipeline for conditions like wet AMD and diabetic retinopathy. [pos]As of March 31, 2025, Ocular Therapeutix reported $12.4 million in cash and cash equivalents. Total debt was $3.44 million. The company has experienced significant stock dilution, with shares outstanding increasing from 76.61 million in 2021 to 159.30 million in June 2025 (a 28.31% increase in Q1 2025). There is no information about stock buybacks.[/pos] [link to Ocular Therapeutix Q1 2025 Earnings Release](https://investors.ocutx.com/news-releases/news-release-details/2025/Ocular-Therapeutix-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to StockAnalysis OCUL Shares Outstanding](https://stockanalysis.com/stocks/ocul/shares-outstanding/)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Very high scalability potential. A successful late-stage trial for its wet AMD treatment would be a major blockbuster opportunity. The hydrogel platform is also scalable to deliver various other drugs for different eye diseases."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Ocular Therapeutix entry updated successfully.")