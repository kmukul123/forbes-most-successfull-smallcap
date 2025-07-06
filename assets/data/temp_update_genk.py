

import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "GEN Restaurant Group":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """GEN Restaurant Group operates a chain of Asian-inspired casual dining restaurants specializing in an all-you-can-eat, 'cook-it-yourself' Korean BBQ experience. The restaurants offer a high-energy, interactive dining atmosphere. [highlight]GEN Restaurant Group's competitive moat is built on its unique and interactive dining experience, value proposition, company-owned growth strategy for brand consistency, and cultural authenticity. It operates in a niche market with few scaled concepts.[/highlight] [pos]GEN Restaurant Group has a Return on Invested Capital (ROIC) of 3.41% (Finance Charts, as of July 2025). Its TTM ROIC was 4.38%, and its 3-year average ROIC was 7.05%. Its ROCE was 0.24% in Q1 2025.[/pos] [neg]However, its TTM ROIC was -0.58% and ROCE was -0.92% (StockAnalysis). Morningstar assigns \"No Economic Moat.\"[/neg] [link to GEN Restaurant Group Investor Relations](https://ir.genkoreanbbq.com/) [link to Finance Charts GENK ROIC](https://financecharts.com/stocks/genk/roic) [link to StockAnalysis GENK ROIC/ROCE](https://stockanalysis.com/stocks/genk/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]The company is controlled by its founders, who hold a significant majority of the ownership and voting power. Specific insider ownership percentages were not readily available from public searches.[/pos]"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company uses debt primarily to finance the build-out of new restaurant locations, which is a capital-intensive process. [pos]As of March 31, 2025, GEN Restaurant Group reported $15.4 million in cash and cash equivalents. Some sources indicate total debt around $6.5 million, while others report higher figures (e.g., $150 million), potentially including lease liabilities. The company announced a $5 million stock repurchase program in March 2025. However, a shelf registration filed in May 2025 indicates potential for significant stock dilution (up to 28.2 million shares) from selling shareholders, which would not provide proceeds to the company.[/pos] [link to GEN Restaurant Group Q1 2025 Earnings Release](https://ir.genkoreanbbq.com/news-releases/news-release-details/2025/GEN-Restaurant-Group-Inc.-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to GEN Restaurant Group Stock Repurchase Program](https://ir.genkoreanbbq.com/news-releases/news-release-details/2025/GEN-Restaurant-Group-Inc.-Announces-Stock-Repurchase-Program/default.aspx)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Highly scalable concept. Growth is achieved by opening new restaurant locations in new and existing markets across the U.S. The concept's strong unit economics and broad appeal support a long runway for expansion."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("GEN Restaurant Group entry updated successfully.")

