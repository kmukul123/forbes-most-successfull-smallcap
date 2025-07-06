

import json

def update_pnrg_description_with_highlights(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for company in data:
        if company.get("TICKER") == "PNRG":
            company["DESCRIPTION"] = {
                "overview": "PrimeEnergy Resources Corporation (NASDAQ: PNRG) is an independent oil and natural gas company involved in the acquisition, development, and production of hydrocarbons, primarily in Texas. [link to Alpha Spread: PNRG Investor Relations](https://alphaspread.com/security/nasdaq/PNRG/investor-relations)",
                "insider_ownership": "[neg]Insider ownership is relatively low, at approximately 4.71% as of June 24, 2025.[/neg] [link to Stock Titan: PrimeEnergy Resources Corporation SEC Filings](https://stocktitan.net/news/PNRG/primeenergy-resources-corporation-announces-first-quarter-2025-financial-results-and-declares-regular-quarterly-cash-dividend-302138033.html)",
                "balancesheet": "[pos]As of December 31, 2023, the company reported zero bank debt.[/pos] Total assets were $339.3 million as of May 2025. [pos]The company has returned $112.6 million to shareholders through stock buybacks since program initiation, retiring approximately 4% of outstanding shares in 2023.[/pos] [link to SEC.gov: ANNUAL REPORT 2023](https://www.sec.gov/Archives/edgar/data/768840/000110465924029000/a23-19000_110k.htm) [link to Nasdaq: PrimeEnergy Resources Corporation SEC Filings](https://www.nasdaq.com/market-activity/stocks/pnrg/sec-filings)",
                "performance": "[pos]Q1 2025 Revenue increased 16.4% year-over-year to $50.1 million, driven by increased oil and gas production (oil up 6%, natural gas up 106.6%, NGL up 120.4%).[/pos] [neg]However, Q1 2025 Net Income decreased to $9.1 million from $11.3 million in Q1 2024, and diluted EPS was $3.72 compared to $4.41 in Q1 2024.[/neg] [link to Nasdaq: PrimeEnergy Resources Corporation SEC Filings](https://www.nasdaq.com/market-activity/stocks/pnrg/sec-filings)"
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
    update_pnrg_description_with_highlights("D:\\users\\mukul\\SharedMukul\\Src\\forbes\\forbes-angular\\src\\assets\\data\\Americas_2025.json")

