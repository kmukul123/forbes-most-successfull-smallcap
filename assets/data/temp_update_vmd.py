
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Viemed Healthcare":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Viemed Healthcare is a provider of in-home respiratory care services and equipment in the United States. It specializes in treating chronic respiratory diseases, such as COPD, by providing non-invasive ventilation therapy and other services. [highlight]Viemed's competitive moat is built on its high-touch, comprehensive in-home care model with licensed Respiratory Therapists, specialization in respiratory healthcare, strong relationships with healthcare systems, and strategic acquisitions.[/highlight] [pos]As of March 2025, Viemed Healthcare's annualized Return on Invested Capital (ROIC) was 3.08% (GuruFocus), and its Return on Capital Employed (ROCE) was 24.29% (StockAnalysis).[/pos] [neg]However, its ROIC of 7.76% (TTM) is below its WACC of 12.14%, suggesting potential value destruction as it grows.[/neg] [link to Viemed Healthcare Investor Relations](https://www.viemed.com/investors/) [link to GuruFocus VMD ROIC](https://www.gurufocus.com/term/roic/NASDAQ:VMD) [link to StockAnalysis VMD ROCE](https://stockanalysis.com/stocks/vmd/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]The CEO and management team have significant ownership stakes, aligning their interests with the company's long-term growth and profitability. Insider ownership is approximately 12.97% (WallStreetZen) to 20.00% (MarketBeat), with Casey Hoyt holding 5.68%.[/pos] [neg]However, insiders have sold more shares than they have purchased over the last three months and 24 months.[/neg] [link to WallStreetZen VMD Ownership](https://www.wallstreetzen.com/stocks/us/nasdaq/vmd/viemed-healthcare/ownership) [link to MarketBeat VMD Insider Trading](https://www.marketbeat.com/stocks/NASDAQ/VMD/insider-trades/)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company maintains a low-debt profile and a strong balance sheet, which supports its organic growth and operational needs. [pos]As of March 31, 2025, Viemed Healthcare reported a cash balance of $10.2 million and long-term debt of $3.5 million. The company has a very low debt-to-equity ratio of 0.00066.[/pos] [pos]Shareholders have not been significantly diluted in the past year. While annual share buybacks are currently reported as $0.00, the Board has historically authorized stock repurchase programs.[/pos] [link to Viemed Healthcare Q1 2025 Earnings Release](https://ir.viemed.com/news-releases/news-release-details/2025/Viemed-Healthcare-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to Simply Wall St VMD Financials](https://simplywall.st/stocks/us/nasdaq/vmd/viemed-healthcare/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Highly scalable due to favorable demographic trends (aging population) and the cost-effectiveness of home-based care. Growth is achieved by expanding its sales force to enter new geographic markets and increasing its referral base from physicians and hospitals."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Viemed Healthcare entry updated successfully.")
