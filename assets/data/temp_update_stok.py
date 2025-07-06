
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Stoke Therapeutics":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Stoke Therapeutics is a clinical-stage biotechnology company focused on treating the underlying cause of severe genetic diseases by upregulating protein expression. Its proprietary TANGO platform is used to develop antisense oligonucleotides for diseases like Dravet syndrome. [highlight]Stoke Therapeutics' competitive moat is built on its proprietary TANGO platform, which enables the development of antisense oligonucleotides to upregulate protein expression, addressing the underlying cause of severe genetic diseases. This unique approach offers a differentiated therapeutic strategy.[/highlight] [pos]Stoke Therapeutics has a Return on Capital Employed (ROCE) of 10.56% and a Return on Invested Capital (ROIC) of 9.54% (StockAnalysis).[/pos] [link to Stoke Therapeutics Investor Relations](https://investors.stoketherapeutics.com/) [link to StockAnalysis STOK ROIC/ROCE](https://stockanalysis.com/stocks/stok/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Backed by leading venture capital firms and institutional biotech investors. Insider ownership is significant, with TipRanks reporting 45.07% and Seth Loring Harrison owning 62.18% of the company's shares.[/pos] [link to TipRanks STOK Ownership](https://www.tipranks.com/stocks/stok/ownership) [link to WallStreetZen STOK Ownership](https://www.wallstreetzen.com/stocks/us/pharmaceuticals-biotechnology/nasdaq-stok/stoke-therapeutics/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """Operates without significant debt, funding its clinical pipeline through equity financing and partnership revenue. [pos]As of March 31, 2025, Stoke Therapeutics reported $380.3 million in cash, cash equivalents, and marketable securities. The company has consistently maintained a strong cash position with minimal to no debt.[/pos] [neg]However, Stoke Therapeutics has experienced significant stock dilution, with shares outstanding increasing from 23.51 million in 2018 to 57.86 million in June 2025 (a 27.55% increase over the last year). There is no information about stock buybacks.[/neg] [link to Stoke Therapeutics Q1 2025 Earnings Release](https://investors.stoketherapeutics.com/news-releases/news-release-details/2025/Stoke-Therapeutics-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to CompaniesMarketCap STOK Shares Outstanding](https://companiesmarketcap.com/stoke-therapeutics/shares-outstanding/)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """The TANGO platform is highly scalable and can be applied to a wide range of genetic diseases caused by protein insufficiency. Success with its lead candidate could validate the platform and unlock numerous other therapeutic programs."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Stoke Therapeutics entry updated successfully.")
