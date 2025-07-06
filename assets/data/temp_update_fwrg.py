
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "First Watch Restaurant Group":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """First Watch is a daytime casual dining restaurant concept serving breakfast, brunch, and lunch. It is known for its menu of fresh, made-to-order dishes and its 'You First' service culture. It operates a large number of company-owned and franchised restaurants. [highlight]First Watch Restaurant Group's competitive moat is built on its unique daytime-only dining concept (optimizes operations, attracts employees), fresh and made-to-order menu with culinary innovation, operational excellence, strong culture, market leadership in the breakfast/brunch segment, aggressive expansion with strong unit economics, and pricing power.[/highlight] [pos]First Watch Restaurant Group has a Return on Invested Capital (ROIC) of 2.01% (GuruFocus, TTM as of May 2025) and a Return on Capital Employed (ROCE) of 2.42% (StockAnalysis). Its ROIC was 1.20% as of December 2024.[/pos] [link to First Watch Restaurant Group Investor Relations](https://investors.firstwatch.com/) [link to GuruFocus FWRG ROIC](https://www.gurufocus.com/term/roic/NASDAQ:FWRG) [link to StockAnalysis FWRG ROIC/ROCE](https://stockanalysis.com/stocks/fwrg/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Primarily owned by private equity and institutional investors. Management holds a smaller stake. Specific insider ownership percentages were not readily available from public searches.[/pos]"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company manages a moderate level of debt, which it uses to finance its aggressive new restaurant opening schedule. [pos]As of March 2025, First Watch Restaurant Group reported $18.6 million in cash, with total debt of $194.6 million, resulting in a net debt of $176.0 million. Its debt increased from $121.7 million in March 2024. The company has experienced negative free cash flow over the last three years. The weighted average number of common shares outstanding (diluted) increased from 59.193 million in 2023 to 62.335 million in 2024, indicating dilution. There is no information about stock buybacks.[/pos] [link to Simply Wall St FWRG Financials](https://simplywall.st/stocks/us/hotels-restaurants-leisure/nasdaq-fwrg/first-watch-restaurant-group/financials) [link to GuruFocus FWRG Debt](https://www.gurufocus.com/term/total_debt/NASDAQ:FWRG)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Highly scalable concept with strong unit economics. Growth is driven by a disciplined strategy of opening new company-owned restaurants in suburban areas across the U.S. The brand's leadership in the growing breakfast and brunch segment provides a long runway for expansion."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("First Watch Restaurant Group entry updated successfully.")
