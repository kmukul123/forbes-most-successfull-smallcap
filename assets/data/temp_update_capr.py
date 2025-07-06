
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Capricor Therapeutics":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Capricor Therapeutics is a clinical-stage biotechnology company focused on the development of cell- and exosome-based therapeutics for the treatment of inflammatory and fibrotic diseases, with a lead program targeting Duchenne muscular dystrophy (DMD). [highlight]Capricor Therapeutics aims to establish a competitive moat through its innovative pipeline, particularly its first-in-class therapy CAP-1002 for DMD cardiomyopathy, which has Orphan Drug designation and a lack of direct competitors. Its focus on rare diseases and robust pipeline contribute to its competitive advantage.[/highlight] [pos]Capricor Therapeutics has a Return on Invested Capital (ROIC) of -47.94% and a Return on Capital Employed (ROCE) of -43.58% (StockAnalysis). Its ROIC excluding Goodwill was -2,419.5% as of March 2025, with a 3-year average of 618.9% and a 5-year average of 524.8%.[/pos] [link to Capricor Therapeutics Investor Relations](https://ir.capricor.com/) [link to StockAnalysis CAPR ROIC/ROCE](https://stockanalysis.com/stocks/capr/roic/) [link to Value Sense CAPR ROIC](https://valuesense.io/stocks/CAPR/roic)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership is substantial, with WallStreetZen reporting 85.20% ownership by insiders, including significant stakes from Nippon Shinyaku Co Ltd (15.51%), Fountainhead Capital Partners Ltd (12.14%), and Cedars Sinai Medical Center (8.86%). Eduardo Marban holds 7.24%. TipRanks reports ~16.79% insider ownership.[/pos] [link to WallStreetZen CAPR Ownership](https://www.wallstreetzen.com/stocks/us/pharmaceuticals-biotechnology/nasdaq-capr/capricor-therapeutics/ownership) [link to TipRanks CAPR Ownership](https://www.tipranks.com/stocks/capr/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """Operates with minimal debt, funding its research and clinical trials primarily through equity raises and government grants. [pos]As of March 31, 2025, Capricor Therapeutics reported approximately $144.8 million in cash, cash equivalents, and marketable securities. The company is largely debt-free, with total debt around $0.84 million (short-term) and $0.41 million (long-term) as of March 2025. Simply Wall St reports $0.0 total debt and a 0% debt-to-equity ratio.[/pos] [neg]However, the company has experienced significant stock dilution, with shares outstanding growing from 4.33 million in 2019 to 45.63 million in 2025, including a 369.61% increase in 2020. An underwritten public offering in October 2024 further diluted shares. There is no information indicating significant share buyback programs.[/neg] [link to Capricor Therapeutics Q1 2025 Earnings Release](https://ir.capricor.com/news-releases/news-release-details/2025/Capricor-Therapeutics-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to CompaniesMarketCap CAPR Shares Outstanding](https://companiesmarketcap.com/capricor-therapeutics/shares-outstanding/)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Extremely high scalability potential if its lead therapy for DMD receives regulatory approval, as it would address a significant unmet medical need. Its exosome technology platform could also be scaled to target other diseases."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Capricor Therapeutics entry updated successfully.")
