

import json

file_path = "D:\\users\\mukul\\SharedMukul\\Src\\forbes\\forbes-angular\\src\\assets\\data\\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "CRA International":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information
        company["DESCRIPTION"]["overview"] = """CRA International (Charles River Associates) is a global consulting firm that offers economic, financial, and management consulting services. It provides expert testimony in litigation and regulatory proceedings and advises clients on business strategy. [highlight]Its competitive moat is built on its reputation for intellectual rigor, the specialized expertise of its consultants, and its ability to provide expert testimony in complex litigation, creating high barriers to entry for competitors.[/highlight]"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership is moderate, with the firm's consultants and executives holding shares. Simply Wall St reports insider ownership at 14.83% as of July 2025, indicating alignment with shareholder interests.[/pos] [link to Simply Wall St CRAI Ownership](https://simplywall.st/stocks/us/commercial-professional-services/nasdaq-crai/charles-river-associates/ownership)"""

        # Update balancesheet (keeping existing info, as new data couldn't be fetched)
        company["DESCRIPTION"]["balancesheet"] = """The company maintains a low-debt balance sheet, using its strong cash flow to reward shareholders through dividends and share buybacks."""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Scalable by hiring more high-caliber consultants and expanding its practice areas (e.g., energy, life sciences, antitrust). Its reputation allows it to command premium fees, and it can scale its operations globally to serve multinational clients."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("CRA International entry updated successfully.")

