
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "AudioEye":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """AudioEye is a technology company that provides a SaaS platform to help businesses make their websites and digital content accessible to individuals with disabilities, ensuring compliance with standards like the Web Content Accessibility Guidelines (WCAG). [pos]AudioEye has a Return on Capital Employed (ROCE) of -14.49% and a Return on Invested Capital (ROIC) of -12.03% (StockAnalysis).[/pos] [link to AudioEye Investor Relations](https://www.audioeye.com/investors/) [link to StockAnalysis AEYE ROIC/ROCE](https://stockanalysis.com/stocks/aeye/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership varies across sources, from 28.80% (MarketBeat) to 73.50% (WallStreetZen). Sero Capital LLC (24.64%) is a significant insider shareholder.[/pos] [link to WallStreetZen AEYE Ownership](https://www.wallstreetzen.com/stocks/us/software/nasdaq-aeye/audioeye/ownership) [link to MarketBeat AEYE Ownership](https://www.marketbeat.com/stocks/NASDAQ/AEYE/institutional-ownership/)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company operates with little to no debt, funding its growth through revenue and equity financing. [pos]As of March 31, 2025, AudioEye reported $8.3 million in cash. Total debt was $11.89 million, resulting in a net cash position of -$3.63 million. AudioEye has actively engaged in share repurchase programs, with a new $12.5 million program announced in January 2025 (expiring January 2027). A previous $5.0 million program in Q4 2023 led to the repurchase of 548,000 shares for $5.73. As of March 31, 2025, 12.45 million shares were outstanding. The 5-Year Share Buyback Ratio was -6.10%.[/pos] [link to AudioEye Q1 2025 Earnings Release](https://www.audioeye.com/news-releases/news-release-details/2025/AudioEye-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to AudioEye Share Repurchase Program](https://www.audioeye.com/news-releases/news-release-details/2025/AudioEye-Announces-New-Share-Repurchase-Program/default.aspx)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Highly scalable SaaS model. Growth is driven by increasing legal and social pressure for digital accessibility. It scales by adding more customers through direct sales and partnerships with web development agencies and other technology platforms."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("AudioEye entry updated successfully.")
