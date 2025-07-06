
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Phreesia":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview
        company["DESCRIPTION"]["overview"] = """Phreesia provides a SaaS platform to automate and manage the patient intake process for healthcare providers. Its solutions include patient registration, insurance verification, and payment collection, and it also has a patient activation solutions business for life sciences companies. [highlight]Phreesia's competitive moat is built on its comprehensive SaaS platform for patient intake, strong network effects within healthcare providers, and its patient activation solutions business for life sciences companies. Its focus on automating and streamlining critical healthcare processes creates high switching costs for clients.[/highlight]"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]The co-founders and management team hold a significant stake, demonstrating a long-term commitment to the company's vision. Insider ownership varies across sources, from 4.72% (Stock Titan) to 26.76% (WallStreetZen).[/pos] [link to Stock Titan PHR Ownership](https://stocktitan.net/news/PHR/phreesia-inc-insider-trades-phr-stock-titan-4-72-insider-ownership-as-of-july-1-2025.html) [link to WallStreetZen PHR Ownership](https://www.wallstreetzen.com/stocks/us/healthcare/nyse-phr/phreesia/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company maintains a strong balance sheet with a healthy cash position and minimal debt, allowing for continued investment in its platform. [pos]As of April 30, 2025, Phreesia reported $90.9 million in cash and cash equivalents, with no outstanding borrowings under its credit facility. Total debt was around $1.6 million. The board approved a 2.5 million share repurchase program, representing approximately 4.2% of outstanding shares if fully utilized. However, the weighted-average common shares outstanding (basic and diluted) increased from 58.277 million in Q4 2025 to 58.920 million in Q1 2026, indicating some dilution, partly due to acquisitions involving common stock.[/pos] [link to Phreesia Q1 2026 Earnings Release](https://ir.phreesia.com/news-releases/news-release-details/2025/Phreesia-Reports-First-Quarter-Fiscal-2026-Results/default.aspx) [link to Simply Wall St PHR Financials](https://simplywall.st/stocks/us/healthcare/nyse-phr/phreesia/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Highly scalable platform. Growth is driven by adding more healthcare providers to its network, cross-selling additional software modules, and growing its high-margin life sciences business. The ongoing need for efficiency in healthcare provides a strong tailwind."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Phreesia entry updated successfully.")
