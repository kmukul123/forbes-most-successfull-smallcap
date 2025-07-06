

import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "SunOpta":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """SunOpta is a company focused on plant-based foods and beverages, and fruit-based foods and ingredients. It is a major producer of oat milk, soy milk, and other plant-based dairy alternatives for private label, co-packing, and its own brands. [highlight]SunOpta's competitive moat is built on its strong market position in plant-based and organic foods, vertical integration and supply chain control, commitment to innovation and sustainability, established relationships with major retailers, and differentiated co-packing expertise.[/highlight] [pos]SunOpta has a Return on Invested Capital (ROIC) of 4.59% and a Return on Capital Employed (ROCE) of 8.31% (StockAnalysis). Its five-year average ROIC was 1.1%.[/pos] [link to SunOpta Investor Relations](https://www.sunopta.com/investors/) [link to StockAnalysis STKL ROIC/ROCE](https://stockanalysis.com/stocks/stkl/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Primarily owned by institutional investors. Insider ownership varies across sources, from 1.55% (TipRanks) to 69.10% (WallStreetZen), with the latter likely including large institutional investors considered \"insiders.\" Simply Wall St indicates insiders have bought more shares than they have sold in the past 3 months.[/pos] [link to TipRanks STKL Ownership](https://www.tipranks.com/stocks/stkl/ownership) [link to WallStreetZen STKL Ownership](https://www.wallstreetzen.com/stocks/us/consumer-defensive/nasdaq-stkl/sunopta/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company carries a significant debt load, which was used to finance the expansion of its manufacturing capacity to meet the booming demand for plant-based products. [pos]As of March 29, 2025, total debt was $260.6 million, a decrease from previous periods. Cash was $2.30 million. Cash provided by operating activities increased to $22.3 million in Q1 2025 from $7.4 million in Q1 2024. SunOpta aims for a leverage target of 2.5x by the end of 2025.[/pos] [neg]SunOpta's diluted weighted-average common shares outstanding increased from 117.558 million in Q1 2024 to 125.007 million in Q1 2025, indicating some stock dilution.[/neg] [pos]However, on May 8, 2025, SunOpta announced a $25 million share repurchase program.[/pos] [link to SunOpta Q1 2025 Earnings Release](https://www.sunopta.com/news-releases/news-release-details/2025/SunOpta-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to SunOpta Share Repurchase Program](https://www.sunopta.com/news-releases/news-release-details/2025/SunOpta-Announces-Share-Repurchase-Program/default.aspx)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Highly scalable by expanding its production capacity and securing long-term contracts with major food retailers and brands. Growth is directly tied to the mainstream adoption of plant-based diets."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("SunOpta entry updated successfully.")
