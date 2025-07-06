
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "International Money Express":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """International Money Express (Intermex) is a leading processor of money transfer services, primarily focusing on the Latin America and Caribbean corridor. It provides a reliable and efficient network for individuals to send money from the U.S. to their home countries. [highlight]International Money Express's competitive moat is built on its strong focus on the US-Latin America and Caribbean (LAC) corridor, extensive agent network, omnichannel service delivery (retail and digital), significant market share in key corridors, and strategic alliances. Its strong return on capital and brand strength further contribute to its competitive edge.[/highlight] [pos]International Money Express has a Return on Capital Employed (ROCE) of 31.70% and a Return on Invested Capital (ROIC) of 19.02% (StockAnalysis). Its ROIC was 38.56% (GuruFocus, TTM as of March 2025).[/pos] [link to Intermex Investor Relations](https://ir.intermexonline.com/) [link to StockAnalysis IMXI ROIC/ROCE](https://stockanalysis.com/stocks/imxi/roic/) [link to GuruFocus IMXI ROIC](https://www.gurufocus.com/term/roic/NASDAQ:IMXI)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]The Chairman and CEO holds a significant stake in the company, demonstrating strong alignment with shareholders. Insider ownership is approximately 6.37% (TipRanks) to 5.69% (GuruFocus).[/pos] [link to TipRanks IMXI Ownership](https://www.tipranks.com/stocks/imxi/ownership) [link to GuruFocus IMXI Ownership](https://www.gurufocus.com/term/insider_ownership/NASDAQ:IMXI)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company operates with a low level of debt, and its business model is highly cash-generative. [pos]As of March 31, 2025, International Money Express reported $151.76 million in cash and cash equivalents, with total debt of $171.27 million, resulting in a net debt position of -$19.51 million. The company has consistently bought back its shares, with $18.783 million in TTM annual share buybacks. A 100,000 share buyback was announced in March 2025. Shares outstanding increased by 1.53% over the last year, indicating some dilution, but buybacks aim to counteract this.[/pos] [link to Intermex Q1 2025 Earnings Release](https://ir.intermexonline.com/news-releases/news-release-details/2025/International-Money-Express-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to Finance Charts IMXI Buybacks](https://financecharts.com/stocks/imxi/buybacks)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Scalable by gaining market share in its core U.S. to Latin America corridor and by expanding its network of paying agents. Growth is also driven by the expansion of its digital and mobile app offerings, which provide a more efficient and scalable way to process transactions."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("International Money Express entry updated successfully.")
