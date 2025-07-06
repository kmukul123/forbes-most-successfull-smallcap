
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "CorMedix":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """CorMedix is a biopharmaceutical company focused on developing and commercializing therapeutic products for the prevention and treatment of infectious and inflammatory diseases. Its lead product, Defencath, is designed to prevent catheter-related bloodstream infections in hemodialysis patients. [highlight]CorMedix's competitive moat is built around its flagship product, DefenCath, which is the first and only FDA-approved antimicrobial catheter lock solution for reducing CRBSIs in hemodialysis patients. It benefits from market exclusivity (QIDP designation), a first-mover advantage, high efficacy (71% reduction in infections), and strong intellectual property (patent protection until 2042).[/highlight] [pos]CorMedix has a Return on Invested Capital (ROIC) of 43.5% (Value Sense, LTM as of March 2025) and a Return on Capital Employed (ROCE) of 12.56% (StockAnalysis). Its annualized ROC for Q1 2025 was 225.65%.[/pos] [link to CorMedix Investor Relations](https://cormedix.com/investor-relations/) [link to Value Sense CRMD ROIC](https://valuesense.io/stocks/CRMD/roic) [link to StockAnalysis CRMD ROIC/ROCE](https://stockanalysis.com/stocks/crmd/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership is moderate, with MarketBeat reporting 7.20% and Trendlyne indicating an increase from 0.86% to 1.46% in May 2025. Insiders have both bought and sold shares recently.[/pos] [link to MarketBeat CRMD Ownership](https://www.marketbeat.com/stocks/NASDAQ/CRMD/institutional-ownership/) [link to Trendlyne CRMD Insider Trading](https://trendlyne.com/equity/share-holding/1400/CRMD/latest/cormedix-inc/)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company has funded its development and regulatory approval process primarily through equity financing and has minimal debt. [pos]CorMedix has maintained a debt-free status ($0.0 total debt) for at least the past five years. As of December 31, 2024, it had $51.7 million in cash and short-term investments, with an expectation of over $75 million by the end of Q1 2025. Its current ratio was 3.39 in Q1 2025. CorMedix recently filed a preliminary prospectus supplement for a common-stock offering of up to $85 million in June 2025, which closed at $82.2 million, indicating stock dilution. There is no information about stock buybacks.[/pos] [link to CorMedix Q1 2025 Earnings Release](https://cormedix.com/news-releases/news-release-details/2025/CorMedix-Inc.-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to Simply Wall St CRMD Financials](https://simplywall.st/stocks/us/pharmaceuticals-biotechnology/nasdaq-crmd/cormedix/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """High scalability upon the successful commercial launch of Defencath. Growth will be driven by securing reimbursement and adoption by dialysis centers. The product addresses a significant unmet medical need with a large target market."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("CorMedix entry updated successfully.")
