import json

file_path = "D:\\users\\mukul\\SharedMukul\\Src\\forbes\\forbes-angular\\src\\assets\\data\\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Natural Grocers Vitamin Cottage":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information
        company["DESCRIPTION"]["overview"] = """Natural Grocers by Vitamin Cottage is a specialty retailer of natural and organic groceries, dietary supplements, and body care products. The company is known for its high-quality standards, affordable prices, and free nutrition education. [highlight]Its strong competitive moat is built on its strict product standards (no artificial colors, flavors, preservatives, or sweeteners; no hydrogenated oils; no factory-farmed meat), which fosters deep customer trust and loyalty. This commitment to quality differentiates it from conventional grocers and even other natural food stores.[/highlight]"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]The founding Isely family maintains majority control of the company through a dual-class share structure, ensuring the company's founding principles are upheld. As of June 2025, insider ownership stands at approximately 27.8%.[/pos] [link to Simply Wall St NGVC Ownership](https://simplywall.st/stocks/us/consumer-retailing/nyse-ngvc/natural-grocers-by-vitamin-cottage/ownership)"""

        # Update balancesheet with cash levels and debt details
        company["DESCRIPTION"]["balancesheet"] = """The company uses debt primarily to finance the opening of new stores and for real estate, but manages its leverage at a reasonable level. [pos]As of March 31, 2025, Natural Grocers reported cash and cash equivalents of $28.5 million.[/pos] [neg]Total debt stood at $100.3 million as of March 31, 2025, primarily related to property leases and store development.[/neg] [link to Natural Grocers Q2 2025 Earnings Release](https://investors.naturalgrocers.com/news-releases/news-release-details/2025/Natural-Grocers-Reports-Second-Quarter-Fiscal-2025-Results/default.aspx)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Scalable through a disciplined new store opening strategy in existing and adjacent states. Growth is also driven by increasing basket size through its [highlight]Npower loyalty program (which had 1.7 million members as of Q2 2025)[/highlight] and expanding its private label offerings. [link to Natural Grocers Q2 2025 Earnings Release](https://investors.naturalgrocers.com/news-releases/news-release-details/2025/Natural-Grocers-Reports-Second-Quarter-Fiscal-2025-Results/default.aspx)"""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Natural Grocers Vitamin Cottage entry updated successfully.")
