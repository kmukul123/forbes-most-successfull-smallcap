
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Ameresco":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information
        company["DESCRIPTION"]["overview"] = """Ameresco is a leading independent provider of comprehensive energy efficiency and renewable energy solutions for facilities throughout North America and Europe. It develops, constructs, and operates projects that reduce energy consumption and generate clean power. [highlight]Ameresco's competitive moat is built on its comprehensive energy solutions, strong relationships with government and institutional clients, and its ability to develop, construct, and operate complex energy projects. Its focus on energy efficiency and renewable energy aligns with global trends, providing a strong tailwind.[/highlight]"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]The founder, President, and CEO holds a substantial majority of the voting power, ensuring a consistent, long-term strategic direction focused on clean energy. Insider ownership is approximately 42.00% (MarketBeat) to 40.50% (TipRanks).[/pos] [link to MarketBeat AMRC Ownership](https://www.marketbeat.com/stocks/NYSE/AMRC/institutional-ownership/) [link to TipRanks AMRC Ownership](https://www.tipranks.com/stocks/amrc/ownership)"""

        # Update balancesheet
        company["DESCRIPTION"]["balancesheet"] = """The company utilizes significant project-based, non-recourse debt to finance the construction of its energy assets, a standard practice in the industry. Specific cash and debt levels, as well as information on stock dilutions or buybacks, were not readily available from public searches."""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Highly scalable, with growth fueled by the global push for decarbonization and energy independence. It scales by winning larger and more complex energy-as-a-service (EaaS) contracts with government, institutional, and commercial customers."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Ameresco entry updated successfully.")
