
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Northwest Pipe":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Northwest Pipe Company is a leading manufacturer of water-related infrastructure products. It specializes in large-diameter, high-pressure engineered steel pipe systems for water transmission and also produces precast concrete products. [highlight]Northwest Pipe's competitive moat is built on its specialized industry leadership in engineered steel water pipe systems, strategic geographic footprint, and essential products with stable demand due to aging infrastructure. The company also benefits from consistent backlog and order book, providing revenue visibility.[/highlight] [pos]Northwest Pipe has a Return on Invested Capital (ROIC) of 7.59% and a Return on Capital Employed (ROCE) of 9.38%. Its ROIC was 9.62% in 2025, up from 5.41% in 2024. Its ROCE was 9.58% in 2025, up from 6.40% in 2024.[/pos] [link to Northwest Pipe Investor Relations](https://nwpipe.com/investors/) [link to Kavout NWPX ROIC](https://kavout.com/stocks/NWPX/roic) [link to MarketBeat NWPX ROCE](https://www.marketbeat.com/stocks/NASDAQ/NWPX/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership is modest, with TipRanks reporting approximately 3.28% and Trendlyne indicating an increase from 3.47% to 3.60% in June 2025.[/pos] [link to TipRanks NWPX Ownership](https://www.tipranks.com/stocks/nwpx/ownership) [link to Trendlyne NWPX Insider Trading](https://trendlyne.com/equity/share-holding/1400/NWPX/latest/northwest-pipe-co/)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """Manages a moderate level of debt, used to finance its manufacturing facilities and working capital for large-scale projects. [pos]As of March 31, 2025, cash and cash equivalents were $5.285 million. The company had outstanding revolving loan borrowings of $25.5 million, with an additional borrowing capacity of approximately $98 million. Its debt is 66% less than its equity, and total debt decreased by 32% year-over-year.[/pos] [pos]In April 2025, Northwest Pipe repurchased approximately 122,000 shares for $5.0 million. A $30 million share repurchase program was authorized in November 2023, and the company intends to continue buybacks as part of its capital allocation strategy.[/pos] [link to Northwest Pipe Q1 2025 Earnings Release](https://nwpipe.com/news-releases/news-release-details/2025/Northwest-Pipe-Company-Announces-First-Quarter-2025-Results/default.aspx) [link to Simply Wall St NWPX Financials](https://simplywall.st/stocks/us/capital-goods/nasdaq-nwpx/northwest-pipe/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Scalability is tied to public infrastructure spending on water systems. Growth is driven by the critical need to repair and upgrade aging water infrastructure in the U.S. The company scales by winning large, multi-year contracts and through strategic acquisitions."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Northwest Pipe entry updated successfully.")
