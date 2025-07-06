
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Genco Shipping & Trading":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Genco Shipping & Trading is a U.S.-based international ship owning company. It transports iron ore, coal, grain, and other drybulk cargoes along worldwide shipping routes with its fleet of modern Capesize, Ultramax, and Supramax vessels. [highlight]Genco Shipping & Trading's competitive moat is built on its comprehensive value strategy (dividends, deleveraging, growth), modern and efficient fleet (42 modern ships), strong financial position with low leverage, scale and diversification as the largest U.S.-headquartered drybulk shipowner, and active commercial strategy.[/highlight] [pos]Genco Shipping & Trading has a Return on Capital Employed (ROCE) of 4.47% and a Return on Invested Capital (ROIC) of 2.67% (StockAnalysis). Its average ROIC over 3 years is 10.82%, and over 5 years, it is 8.54%.[/pos] [link to Genco Shipping & Trading Investor Relations](https://ir.gencoshipping.com/) [link to StockAnalysis GNK ROIC/ROCE](https://stockanalysis.com/stocks/gnk/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership is moderate, with WallStreetZen reporting 30.09% and TipRanks reporting 1.72%. Key insider shareholders include Strategic Value Partners LLC (6.97%) and B. James Ford (6.88%).[/pos] [link to WallStreetZen GNK Ownership](https://www.wallstreetzen.com/stocks/us/industrials/nyse-gnk/genco-shipping-trading/ownership) [link to TipRanks GNK Ownership](https://www.tipranks.com/stocks/gnk/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company has pursued an aggressive deleveraging strategy and now maintains one of the lowest debt profiles in the drybulk shipping industry, allowing for a high-dividend payout strategy. [pos]As of March 29, 2025, Genco Shipping & Trading reported $20.6 million in cash and cash equivalents, with outstanding debt at $740.0 million. The company has a strong financial position with low financial leverage and a low net loan-to-value ratio (6%).[/pos] [pos]In Q1 2025, the Board approved a new $50 million share repurchase program. The number of shares outstanding has increased by 1.53% over the last year, indicating some dilution, but the buyback program aims to counteract this.[/pos] [link to Genco Shipping & Trading Q1 2025 Earnings Release](https://ir.gencoshipping.com/news-releases/news-release-details/2025/Genco-Shipping--Trading-Limited-Announces-First-Quarter-2025-Financial-Results/default.aspx) [link to Simply Wall St GNK Financials](https://simplywall.st/stocks/us/industrials/nyse-gnk/genco-shipping-trading/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Scalability is cyclical and tied to global drybulk shipping rates. The company's value-oriented strategy focuses on fleet renewal and returning capital to shareholders rather than growth at any cost. It can scale its fleet through opportunistic vessel acquisitions."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Genco Shipping & Trading entry updated successfully.")
