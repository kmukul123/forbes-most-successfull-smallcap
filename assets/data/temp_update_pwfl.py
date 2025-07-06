
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Powerfleet":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Powerfleet is a global provider of wireless Internet of Things (IoT) and machine-to-machine (M2M) solutions for securing, controlling, tracking, and managing high-value enterprise assets, such as industrial trucks, trailers, and cargo. [highlight]Powerfleet's competitive moat is built on its proprietary Unity Platform (device-agnostic data ingestion, AI/ML for insights), a subscription-based SaaS model for recurring revenue, integrated and comprehensive solutions, and strategic acquisitions (e.g., MiX Telematics, Fleet Complete) for scale and market leadership.[/highlight] [pos]Powerfleet has a Return on Invested Capital (ROIC) of -5.88% (GuruFocus, TTM as of May 2025). Its ROIC was -0.89% for Q4 2024.[/pos] [link to Powerfleet Investor Relations](https://ir.powerfleet.com/) [link to GuruFocus PWFL ROIC](https://www.gurufocus.com/term/roic/NASDAQ:PWFL)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership is moderate, with Stock Titan reporting 9.01%. Institutional ownership is higher, with 122,161,195 shares held by 346 institutional owners.[/pos] [link to Stock Titan PWFL Ownership](https://stocktitan.net/news/PWFL/powerfleet-inc-insider-trades-pwfl-stock-titan-9-01-insider-ownership-as-of-july-1-2025.html) [link to Fintel PWFL Ownership](https://fintel.io/n/us/pwfl)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company has used debt to help finance its strategic acquisitions, which have significantly expanded its global footprint and technology capabilities. [pos]As of March 31, 2025, Powerfleet reported $31.4 million in cash and short-term investments, with total debt of $139.6 million, resulting in a net debt of $108.2 million. Its debt-to-equity ratio was 61.3% (increased from 26.3% over 5 years). The company has a sufficient cash runway for more than a year. Recent acquisitions (MiX Telematics, Fleet Complete) have led to significant stock dilution, with Powerfleet securityholders expected to own approximately 34.5% of the combined company with MiX Telematics on a fully diluted basis. The company repaid $2.6 million in long-term debt in Q1 2025.[/pos] [link to Powerfleet Q1 2025 Earnings Release](https://ir.powerfleet.com/news-releases/news-release-details/2025/Powerfleet-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to Simply Wall St PWFL Financials](https://simplywall.st/stocks/us/technology/nasdaq-pwfl/powerfleet/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Highly scalable SaaS and device model. Growth is driven by the increasing need for visibility and efficiency in logistics and supply chain management. It scales by adding more assets to its platform, generating recurring subscription revenue."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Powerfleet entry updated successfully.")
