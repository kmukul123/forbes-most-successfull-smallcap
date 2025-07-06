

import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Igm Biosciences":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """IGM Biosciences is a clinical-stage biotechnology company pioneering the development of engineered IgM antibodies. Its platform aims to create more effective therapeutics for treating cancer, infectious diseases, and autoimmune disorders. [highlight]IGM Biosciences' competitive moat is primarily built on its proprietary IgM antibody technology platform, which allows for stronger binding and potentially enhanced efficacy compared to conventional antibodies. The company has overcome historical manufacturing challenges, built a strong intellectual property portfolio, and has a differentiated therapeutic approach. A strategic collaboration with Sanofi further validates its technology and provides funding.[/highlight] [neg]However, GuruFocus suggests it has \"No Moat - Very weak/transient advantages.\"[/neg] [pos]For Igm Biosciences, the Return on Capital Employed (ROCE) is -96.00%, and the Return on Invested Capital (ROIC) is -86.87%.[/pos] [link to IGM Biosciences Investor Relations](https://ir.igmbio.com/) [link to StockAnalysis IGMS ROIC/ROCE](https://stockanalysis.com/stocks/igms/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership is significant at 38.81% (Stock Titan), indicating strong alignment with shareholder interests.[/pos] [link to Stock Titan IGMS Ownership](https://stocktitan.net/news/IGMS/igm-biosciences-inc-insider-trades-igms-stock-titan-38-81-insider-ownership-as-of-july-1-2025.html)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """As a clinical-stage biotech, it relies on equity financing and strategic partnership funding rather than traditional debt to fund its extensive R&D pipeline. [pos]IGM Biosciences is largely debt-free, with Simply Wall St reporting $0.0 total debt. As of March 31, 2025, cash and investments were $218.8 million, with a net cash position of $108.15 million (Stock Analysis).[/pos] [neg]The company has experienced stock dilutions, with an offering of common stock and non-voting common stock in June 2023. Shares outstanding were 61,162,762 as of June 2025.[/neg] [pos]IGM Biosciences has a share repurchase program, though its buyback yield is low compared to peers.[/pos] [link to IGM Biosciences Q1 2025 Earnings Release](https://ir.igmbio.com/news-releases/news-release-details/2025/IGM-Biosciences-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to Simply Wall St IGMS Financials](https://simplywall.st/stocks/us/pharmaceuticals-biotechnology/nasdaq-igms/igm-biosciences/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Potentially very high scalability if its IgM platform technology is validated in clinical trials. A successful drug could lead to a pipeline of new candidates across multiple diseases. Scalability is currently dependent on clinical success and manufacturing capabilities."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Igm Biosciences entry updated successfully.")
