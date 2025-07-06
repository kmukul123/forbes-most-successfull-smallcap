
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Quinstreet":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """QuinStreet is a performance marketing company. It operates online marketplaces that match consumers with products and services in verticals like financial services (insurance, credit cards) and home services. [highlight]Its competitive moat is derived from its proprietary technology platform, extensive data assets, and deep expertise in performance marketing across specialized verticals.[/highlight] [pos]As of March 31, 2025, QuinStreet reported a Return on Capital Employed (ROCE) of 1.9% and a Return on Invested Capital (ROIC) of 1.8%.[/pos] [link to GuruFocus QNST ROIC/ROCE](https://www.gurufocus.com/term/roic/NASDAQ:QNST)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]The CEO and founder holds a substantial portion of the company's stock, indicating strong leadership alignment and a long-term strategic focus. Insider ownership is approximately 1.9%.[/pos] [link to Simply Wall St QNST Ownership](https://simplywall.st/stocks/us/media/nasdaq-qnst/quinstreet/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock buybacks
        company["DESCRIPTION"]["balancesheet"] = """QuinStreet operates with no long-term debt and maintains a strong cash position, allowing it to invest in its technology platform and explore strategic opportunities. [pos]As of March 31, 2025, cash and cash equivalents were $40.1 million, with no long-term debt.[/pos] [pos]The company has a history of share repurchases, with $10.0 million authorized for buybacks in 2024.[/pos] [link to QuinStreet Q1 2025 Earnings Release](https://investor.quinstreet.com/news-releases/news-release-details/2025/QuinStreet-Reports-First-Quarter-Fiscal-2025-Results/default.aspx)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Highly scalable technology-based model. Growth is achieved by expanding into new client verticals, optimizing its media buying and conversion funnels, and leveraging its vast dataset to improve targeting and performance for its clients."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Quinstreet entry updated successfully.")
