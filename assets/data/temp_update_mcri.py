
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Monarch Casino & Resort":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Monarch Casino & Resort owns and operates two hotel casino properties: the Atlantis Casino Resort Spa in Reno, Nevada, and the Monarch Casino Resort Spa in Black Hawk, Colorado. The company focuses on providing a high-quality, luxury gaming and resort experience. [highlight]Monarch Casino & Resort's competitive moat is built on its established brand, high-quality luxury gaming and resort experience, and strategic locations. Its focus on providing a premium experience and its active stock repurchase program contribute to its value proposition.[/highlight] [pos]Monarch Casino & Resort has a Return on Capital Employed (ROCE) of 21.77% and a Return on Invested Capital (ROIC) of 12.06% (GuruFocus, TTM). Its annualized ROIC for Q1 2025 was 12.95%.[/pos] [link to Monarch Casino & Resort Investor Relations](https://www.monarchcasino.com/investor-relations/) [link to StockAnalysis MCRI ROIC/ROCE](https://stockanalysis.com/stocks/mcri/roic/) [link to GuruFocus MCRI ROIC](https://www.gurufocus.com/term/roic/NASDAQ:MCRI)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]The founding Farahi family owns a large, controlling stake in the company, ensuring a very long-term, conservative, and quality-focused management approach. Insider ownership is significant, with WallStreetZen reporting 65.48% and TipRanks reporting 22.86%. John Farahi (29.48%), Ben Farahi (23.25%), and Bob Farahi (12.14%) are key insider shareholders.[/pos] [link to WallStreetZen MCRI Ownership](https://www.wallstreetzen.com/stocks/us/consumer-cyclical/nasdaq-mcri/monarch-casino-resort/ownership) [link to TipRanks MCRI Ownership](https://www.tipranks.com/stocks/mcri/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company used significant debt to finance the major expansion of its Black Hawk property but is now rapidly paying it down with its strong free cash flow. [pos]Monarch Casino & Resort has an active stock repurchase plan, with authorization to buy back up to 3,000,000 shares. In Q2 2024, 452,464 shares were purchased for $30.5 million, and in Q3 2024, 131,285 shares were purchased for $9.6 million. These buybacks are financed through operating cash flows, cash on hand, and credit facility borrowings. There is no indication of active stock dilution.[/pos] [link to Monarch Casino & Resort Q3 2024 Earnings Release](https://www.monarchcasino.com/news-releases/news-release-details/2024/Monarch-Casino--Resort-Inc.-Reports-Third-Quarter-2024-Results/default.aspx) [link to SEC.gov MCRI Filings](https://www.sec.gov/Archives/edgar/data/815690/000110465924029000/a23-19000_10k.htm)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Scalability is limited by its two-property portfolio. Future growth would likely require a major acquisition or new development project. Near-term growth is focused on optimizing the performance and maximizing the cash flow of its newly expanded Colorado property."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Monarch Casino & Resort entry updated successfully.")
