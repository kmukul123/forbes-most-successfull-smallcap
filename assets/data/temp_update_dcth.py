

import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Delcath Systems":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Delcath Systems is an interventional oncology company focused on the treatment of primary and metastatic liver cancers. Its proprietary system, the CHEMOSAT Hepatic Delivery System, is designed to deliver high-dose chemotherapy directly to the liver. [highlight]Delcath's competitive moat is primarily built on its proprietary technology (HEPZATO KIT for targeted liver chemotherapy), and high regulatory and patent barriers (patents for HEPZATO extend until at least 2032). It targets a specific, unmet medical need.[/highlight] [neg]However, the moat is challenged by limited efficacy, treatment complexity, and emerging competition. GuruFocus suggests \"No Moat\" or \"Very weak/transient advantages.\"[/neg] [pos]Delcath Systems has a Return on Invested Capital (ROIC) of -1.69% and a Return on Capital Employed (ROCE) of -1.82% (StockAnalysis).[/pos] [link to Delcath Systems Investor Relations](https://www.delcath.com/investors/) [link to StockAnalysis DCTH ROIC/ROCE](https://stockanalysis.com/stocks/dcth/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Primarily owned by institutional and retail investors. Insider ownership varies across sources, from 11.6% (Simply Wall St) to 31.28% (TipRanks).[/pos] [link to Simply Wall St DCTH Ownership](https://simplywall.st/stocks/us/pharmaceuticals-biotechnology/nasdaq-dcth/delcath-systems/ownership) [link to TipRanks DCTH Ownership](https://www.tipranks.com/stocks/dcth/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company has historically funded its long development and regulatory process through equity and convertible debt offerings. [pos]As of March 2025, Delcath Systems had approximately $59 million in cash and no reported long-term debt. GuruFocus reported cash per share at $1.76 as of March 2025. Simply Wall St reports $0.0 total debt and a 0% debt-to-equity ratio.[/pos] [link to Simply Wall St DCTH Financials](https://simplywall.st/stocks/us/pharmaceuticals-biotechnology/nasdaq-dcth/delcath-systems/financials) [link to GuruFocus DCTH Financials](https://www.gurufocus.com/term/cash_per_share/NASDAQ:DCTH)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """High scalability upon successful commercial launch and adoption of its treatment system. Growth is driven by gaining reimbursement, expanding into new markets, and proving its efficacy in treating various liver-dominant cancers."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Delcath Systems entry updated successfully.")

