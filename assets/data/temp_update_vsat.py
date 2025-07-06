
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "ViaSat":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Viasat is a global communications company. It provides high-speed satellite broadband services and secure networking systems for military and commercial markets. It designs and operates its own high-capacity communications satellites. [highlight]ViaSat's competitive moat is built on its advanced satellite technology (ViaSat-1, -2, -3 constellations), vertically integrated infrastructure, established customer base and strategic partnerships, focus on high-value markets (aviation, government), innovation and technical expertise, diversification across markets, and bandwidth economics.[/highlight] [pos]ViaSat has a Return on Invested Capital (ROIC) of 0.36% (StockAnalysis, TTM). Its annualized ROIC for Q1 2025 was -4.47%. Its ROCE was 0.52%.[/pos] [link to ViaSat Investor Relations](https://investor.viasat.com/) [link to StockAnalysis VSAT ROIC/ROCE](https://stockanalysis.com/stocks/vsat/roic/) [link to GuruFocus VSAT ROIC](https://www.gurufocus.com/term/roic/NASDAQ:VSAT)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership is moderate, with Trendlyne reporting 0.64% and GuruFocus reporting 1.09%. The co-founder and executive chairman play a key role in the company's long-term technology strategy.[/pos] [link to Trendlyne VSAT Ownership](https://trendlyne.com/equity/share-holding/1400/VSAT/latest/viasat-inc/) [link to GuruFocus VSAT Ownership](https://www.gurufocus.com/term/insider_ownership/NASDAQ:VSAT)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company carries a very large amount of debt, used to finance the construction and launch of its multi-billion dollar satellite constellations. [pos]As of March 2025, ViaSat had $1.6 billion in cash and short-term investments, with total debt of $6.88 billion, resulting in a net debt of $5.27 billion. Its debt-to-equity ratio is 148.1%, considered high. The company has a stock buyback program, with recent repurchases including $2.80 million in December 2024. It has also been repurchasing its debt (e.g., $50.5 million of 2025 notes and $101.7 million of 2026 notes in September 2024). Shares outstanding were 130.32 million as of April 2024, with diluted EPS at -$4.45 (TTM).[/pos] [link to ViaSat Q4 2025 Earnings Release](https://investor.viasat.com/news-releases/news-release-details/2025/Viasat-Reports-Fourth-Quarter-and-Fiscal-Year-2025-Financial-Results/default.aspx) [link to Simply Wall St VSAT Financials](https://simplywall.st/stocks/us/communication-services/nasdaq-vsat/viasat/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Extremely high scalability. The capacity of its satellite network can serve millions of users, and adding a new customer has a very low marginal cost. Growth is driven by selling more broadband plans for residential, in-flight, and government use. The business model is capital-intensive upfront but highly scalable once the satellites are in orbit."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("ViaSat entry updated successfully.")
