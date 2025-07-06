

import json

def update_egy_description_with_highlights(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for company in data:
        if company.get("TICKER") == "EGY":
            company["DESCRIPTION"] = {
                "overview": "Vaalco Energy, Inc. (NYSE: EGY; LSE: EGY) is an independent exploration and production (E&P) energy company with assets in Côte d'Ivoire, Egypt, Equatorial Guinea, Gabon, and Canada. Founded in 1985 and headquartered in Houston, Texas. [link to Vaalco Energy Investor Relations](https://www.vaalco.com/investors)",
                "insider_ownership": "[neg]Insider ownership is relatively low, varying from 1.30% to 13.88% across different sources.[/neg] [link to MarketBeat: Vaalco Energy Insider Ownership](https://www.marketbeat.com/stocks/NYSE/EGY/insider-trades/) [link to TipRanks: Vaalco Energy Insider Trading](https://www.tipranks.com/stocks/egy/insider-trading)",
                "balancesheet": "[pos]As of March 31, 2025, Vaalco had an unrestricted cash balance of $40.9 million and reported zero bank debt as of December 31, 2023.[/pos] The company also secured a new reserves-based revolving credit facility of $190 million (expandable to $300 million). [link to Nasdaq: Vaalco Energy Q1 2025 Earnings](https://www.nasdaq.com/press-release/vaalco-energy-announces-first-quarter-2025-financial-and-operating-results-20250507-0)",
                "performance": "[pos]Q1 2025 Revenue increased 16.4% year-over-year to $50.1 million, driven by increased oil and natural gas production (oil up 6%, natural gas up 106.6%, NGL up 120.4%).[/pos] [neg]However, Q1 2025 Net Income decreased to $9.1 million from $11.3 million in Q1 2024, and diluted EPS was $3.72 compared to $4.41 in Q1 2024.[/neg] [pos]The company has returned $112.6 million to shareholders through stock buybacks since program initiation.[/pos] [link to Nasdaq: Vaalco Energy Q1 2025 Earnings](https://www.nasdaq.com/press-release/vaalco-energy-announces-first-quarter-2025-financial-and-operating-results-20250507-0)"
            }
            # Rename keys as requested
            if "main" in company["DESCRIPTION"]:
                company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
            if "debt" in company["DESCRIPTION"]:
                company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")
            break

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    update_egy_description_with_highlights("D:\\users\\mukul\\SharedMukul\\Src\\forbes\\forbes-angular\\src\\assets\\data\\Americas_2025.json")

