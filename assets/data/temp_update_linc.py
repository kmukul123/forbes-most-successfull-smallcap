

import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Lincoln Educational Services":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Lincoln Educational Services is a provider of career-oriented post-secondary education, primarily in the skilled trades. It offers programs in automotive technology, skilled trades (like welding and electrical), healthcare, and IT at campuses across the U.S. [highlight]Lincoln Educational Services' competitive moat is built on its focus on addressing the \"skills gap\" in the American workforce, strong industry partnerships (e.g., Tesla, Ford, NASA), hands-on training, established reputation (founded 1946), diversified program offerings, and strategic expansion.[/highlight] [pos]Lincoln Educational Services has a Return on Capital Employed (ROCE) of 5.2% as of March 2025. Its annualized Return on Invested Capital (ROIC) was 2.33% for the quarter ending March 2025, with a trailing twelve-month (TTM) ROIC of 3.70%.[/pos] [link to Lincoln Educational Services Investor Relations](https://www.lincolneducationalservices.com/investors/) [link to Simply Wall St LINC ROCE](https://simplywall.st/stocks/us/consumer-services/nasdaq-linc/lincoln-educational-services/financials) [link to GuruFocus LINC ROIC](https://www.gurufocus.com/term/roic/NASDAQ:LINC)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership is moderate, with the company primarily held by institutional investors. Specific insider ownership percentages were not readily available from public searches.[/pos]"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """Manages its debt levels, which are primarily related to campus leases and investments in training equipment, prudently. [pos]As of March 31, 2025, Lincoln Educational Services reported approximately $28.66 million in cash and cash equivalents and no outstanding debt. As of December 31, 2024, it had nearly $60 million in cash and no outstanding debt, with total liquidity of nearly $100 million. The company has shown a strong focus on maintaining a debt-free balance sheet.[/pos] [link to Lincoln Educational Services Q1 2025 Earnings Release](https://www.lincolneducationalservices.com/news-releases/news-release-details/2025/Lincoln-Educational-Services-Reports-First-Quarter-2025-Results/default.aspx)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Scalable by expanding high-demand programs, increasing student enrollment, and building partnerships with corporations that need skilled workers. Growth is fueled by the persistent skills gap in the U.S. economy."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Lincoln Educational Services entry updated successfully.")
