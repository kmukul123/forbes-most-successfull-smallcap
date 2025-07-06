
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "AnaptysBio":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """AnaptysBio is a clinical-stage biotechnology company focused on developing antibody therapeutics for inflammatory diseases. Its pipeline includes candidates for conditions like atopic dermatitis and asthma, developed using its proprietary antibody discovery platform. [highlight]AnaptysBio's competitive moat is built on its innovative drug pipeline, particularly rosnilimab (potential blockbuster for rheumatoid arthritis and ulcerative colitis), differentiation through strong clinical performance, strategic focus on core programs, and proven drug discovery capabilities (e.g., dostarlimab licensed to GSK).[/highlight] [neg]However, it faces intense competition and has negative ROIC/ROCE, indicating inefficiencies in capital utilization.[/neg] [pos]AnaptysBio has a Return on Invested Capital (ROIC) of -16.60% and a Return on Capital Employed (ROCE) of -26.53% (StockAnalysis).[/pos] [link to AnaptysBio Investor Relations](https://ir.anaptysbio.com/) [link to StockAnalysis ANAB ROIC/ROCE](https://stockanalysis.com/stocks/anab/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Primarily owned by institutional biotech investors. Insider ownership is approximately 43.85% (TipRanks).[/pos] [link to TipRanks ANAB Ownership](https://www.tipranks.com/stocks/anab/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company has a strong, debt-free balance sheet with a large cash position derived from partnerships and equity financing, which funds its clinical trials. [pos]As of December 31, 2024, AnaptysBio reported $420.8 million in cash, cash equivalents, and investments. As of March 2025, total debt was $330.4 million, resulting in a net cash position of $9.55 million. Its debt-to-equity ratio increased from 0% to 971.1% over the past five years. The company has a sufficient cash runway for more than three years. There is no information about stock dilutions or buybacks.[/pos] [link to AnaptysBio Q4 2024 Earnings Release](https://ir.anaptysbio.com/news-releases/news-release-details/2025/AnaptysBio-Reports-Fourth-Quarter-and-Full-Year-2024-Financial-Results/default.aspx) [link to Simply Wall St ANAB Financials](https://simplywall.st/stocks/us/pharmaceuticals-biotechnology/nasdaq-anab/anaptysbio/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Scalable through successful clinical development and potential out-licensing or commercialization of its drug candidates. Its antibody generation platform can also be used to create a pipeline of new therapeutics."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("AnaptysBio entry updated successfully.")
