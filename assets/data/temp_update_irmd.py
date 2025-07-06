

import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Iradimed":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """IRADIMED develops, manufactures, and markets Magnetic Resonance Imaging (MRI) compatible medical devices. Its main products include non-magnetic IV infusion pump systems and patient monitoring systems designed for use within the powerful magnetic field of an MRI scanner. [highlight]Iradimed possesses a strong competitive moat due to its highly specialized focus and technological leadership in the niche market of MRI-compatible medical devices. It is considered the \"only known provider\" of a non-magnetic IV infusion pump system for MRI, with proprietary technology, regulatory barriers (FDA clearances), and high implied switching costs for hospitals.[/highlight] [pos]Iradimed has demonstrated strong returns on capital, with a Return on Capital Employed (ROCE) of 24.29% and a Return on Invested Capital (ROIC) of 38.81% as of July 2025 (Finance Charts), with a 3-year average ROIC of 48.44%.[/pos] [link to Iradimed Investor Relations](https://ir.iradimed.com/) [link to Finance Charts IRMD ROIC](https://financecharts.com/stocks/irmd/roic)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Iradimed's ownership is significantly held by insiders (41.08%), with Roger E. Susi, the largest individual shareholder, holding 36.08% of the company's shares, indicating strong alignment with shareholder interests.[/pos] [neg]However, insiders have sold more shares than they have purchased over the last 24 months.[/neg] [link to WallStreetZen IRMD Ownership](https://www.wallstreetzen.com/stocks/us/nyse/irmd/iradimed-corp/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company is completely debt-free and has a substantial cash reserve, which allows it to fully fund its R&D and sales expansion internally. [pos]As of March 31, 2025, Iradimed reported total cash and cash equivalents of $50.33 million, with total debt of only $60,000, resulting in a net cash position of $50.27 million. The debt-to-equity ratio is a very low 0.00066.[/pos] [pos]Shareholders have not been significantly diluted in the past year. While annual share buybacks are currently reported as $0.00, the Board has historically authorized stock repurchase programs.[/pos] [link to Forbes IRMD Financials](https://www.forbes.com/companies/iradimed/) [link to Financial Modeling Prep IRMD Debt-to-Equity](https://financialmodelingprep.com/financial-statements/IRMD)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Scalable by expanding its international sales network and by developing new, innovative MRI-compatible devices. As the only provider of a non-magnetic IV pump, it has a strong competitive moat, and growth comes from increasing penetration in hospitals and imaging centers worldwide."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Iradimed entry updated successfully.")
