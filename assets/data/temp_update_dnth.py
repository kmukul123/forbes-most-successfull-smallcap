

import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Dianthus Therapeutics":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Dianthus Therapeutics is a clinical-stage biotechnology company focused on developing next-generation antibody therapies for severe autoimmune diseases. Its lead product candidates target the classical complement pathway, which is implicated in various disorders. [highlight]Dianthus Therapeutics' competitive moat is primarily built on its differentiated product candidate DNTH103, which offers a unique mechanism of action and improved dosing/administration (less frequent, subcutaneous injections). It also has \"pipeline-in-a-product\" potential across various autoimmune disorders and a robust patent portfolio (expiring no earlier than 2043).[/highlight] [neg]However, as a clinical-stage company, it faces significant competition, regulatory risks, and has incurred operating losses. GuruFocus suggests it has \"No Moat - Very weak/transient advantages.\"[/neg] [pos]For Dianthus Therapeutics, the Return on Capital Employed (ROCE) is -35.34% and the Return on Invested Capital (ROIC) is -20.83% (StockAnalysis).[/pos] [link to Dianthus Therapeutics Investor Relations](https://www.dianthustx.com/investors/) [link to StockAnalysis DNTH ROIC/ROCE](https://stockanalysis.com/stocks/dnth/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership is approximately 8.15% (MarketBeat), with Fairmount Funds Management Llc and Simrat Randhawa being key insiders. Insiders have purchased over $1.3 million in shares in the last 24 months.[/pos] [link to MarketBeat DNTH Ownership](https://www.marketbeat.com/stocks/NASDAQ/DNTH/institutional-ownership/)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """Operates without significant debt, funding its pipeline through equity financing. [pos]Forbes reports total cash of $263.23 million and total debt of $1.4 million, resulting in a net cash position of $330.14 million. Simply Wall St indicates the company is \"debt free\" and has had no debt for the past five years. This financial runway is expected to extend into the second half of 2027.[/pos] [neg]Dianthus Therapeutics has experienced stock dilution through mixed shelf offerings and \"at the market offerings,\" with shares outstanding increasing from 25.665 million in March 2024 to 35.790 million in March 2025. There is no information about stock buybacks.[/neg] [link to Forbes DNTH Financials](https://www.forbes.com/companies/dianthus-therapeutics/) [link to Dianthus Therapeutics SEC Filings](https://www.dianthustx.com/investors/sec-filings/default.aspx)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """High scalability potential if its complement-inhibiting antibodies prove successful in clinical trials. The platform could be applied to a range of rare and severe autoimmune conditions, creating a pipeline of valuable assets."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Dianthus Therapeutics entry updated successfully.")
