
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "The Hackett Group":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """The Hackett Group is a strategic advisory and technology consulting firm. It provides best practice intelligence, benchmarking, and transformation consulting to global companies, with a focus on areas like finance, IT, and human resources. [highlight]The Hackett Group maintains a competitive moat primarily through its extensive benchmarking database (data from Dow Jones Industrials and Fortune 100 companies), deep industry expertise, proven methodologies, and focus on delivering tangible ROI through AI-driven platforms (AI XPLR™, ZBrain™).[/highlight] [pos]The Hackett Group has a Return on Capital Employed (ROCE) of 25.92% and a Return on Invested Capital (ROIC) of 17.94% (StockAnalysis). Its ROIC was 15.82% as of TTM June 2025.[/pos] [link to The Hackett Group Investor Relations](https://www.thehackettgroup.com/investors/) [link to StockAnalysis HCKT ROIC/ROCE](https://stockanalysis.com/stocks/hckt/roic/) [link to GuruFocus HCKT ROIC](https://www.gurufocus.com/term/roic/NASDAQ:HCKT)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]The co-founders and key executives hold a significant portion of the company's stock, ensuring strong alignment with shareholder interests. Insider ownership is approximately 15.40% (MarketBeat). There has been no insider buying or selling in the last three months.[/pos] [link to MarketBeat HCKT Ownership](https://www.marketbeat.com/stocks/NASDAQ/HCKT/institutional-ownership/)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company operates with little to no debt, using its strong cash flow to fund its operations and return capital to shareholders via dividends and buybacks. [pos]As of March 2025, The Hackett Group had $9.17 million in cash on hand. Total debt was approximately $18.32 million (CompaniesMarketCap). As of December 2024, cash balances were $16.4 million with $13.0 million outstanding on its credit facility. The company repurchased 379,000 shares for $11.7 million in Q1 2025, and 117,000 shares for $3.6 million in Q4 2024. Approximately $21.3 million remained available under its share repurchase program as of Q1 2025. The number of shares outstanding decreased by 2.65% over one year.[/pos] [link to The Hackett Group Q1 2025 Earnings Release](https://www.thehackettgroup.com/news-releases/news-release-details/2025/The-Hackett-Group-Announces-First-Quarter-2025-Results/default.aspx) [link to StockAnalysis HCKT Financials](https://stockanalysis.com/stocks/hckt/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Scalable by leveraging its proprietary intellectual property (the Hackett benchmarks) across its consulting engagements. Growth comes from expanding its client base and selling higher-value, technology-enabled transformation services."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("The Hackett Group entry updated successfully.")
