import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "C4 Therapeutics":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """C4 Therapeutics is a clinical-stage biopharmaceutical company focused on advancing a new class of medicines called targeted protein degraders. Its TORPEDO platform is used to design small-molecule drugs that direct the body's natural machinery to destroy disease-causing proteins. [pos]C4 Therapeutics has a Return on Invested Capital (ROIC) of -171.3% and a Return on Capital Employed (ROCE) of -39.3% (Value Sense). Stock Analysis reports ROIC as -24.80% and ROCE as -41.82%.[/pos] [link to C4 Therapeutics Investor Relations](https://ir.c4therapeutics.com/) [link to Value Sense CCCC ROIC/ROCE](https://valuesense.io/stocks/CCCC/roic) [link to StockAnalysis CCCC ROIC/ROCE](https://stockanalysis.com/stocks/cccc/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """Supported by a strong syndicate of biotech investors and pharmaceutical partners. Management and scientific founders hold stakes in the company. Specific insider ownership percentages were not readily available from public searches."""

        # Update balancesheet with cash levels and debt details
        company["DESCRIPTION"]["balancesheet"] = """Primarily funded through equity and collaboration payments from partners like Roche and Biogen, rather than carrying significant debt. [pos]As of March 31, 2025, C4 Therapeutics reported $234.7 million in cash, cash equivalents, and marketable securities. Total debt was $65.76 million as of December 31, 2024. The company has shown decreasing debt levels and is primarily financed by equity.[/pos]"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """The platform technology is highly scalable and can be applied to a wide range of previously 'undruggable' protein targets in oncology and other diseases. Long-term scalability depends on clinical validation and successful partnerships."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("C4 Therapeutics entry updated successfully.")