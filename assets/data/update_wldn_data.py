import json

def update_wldn_description_with_highlights(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for company in data:
        if company.get("TICKER") == "WLDN":
            company["DESCRIPTION"] = {
                "overview": "Willdan Group is a professional services firm providing technical and consulting services to utilities, government agencies, and private industry. Its core focus is on energy efficiency, grid modernization, and engineering for public infrastructure. [pos]The company was founded in 1964 and is headquartered in Anaheim, California, with 1761 employees as of December 27, 2024, indicating a well-established and substantial operation.[/pos] [link to Willdan Group Investor Relations](https://www.willdangroup.com/)",
                "insider_ownership": "Insider ownership is moderate, with TipRanks indicating approximately 17.82% of the company's stock is owned by insiders. [link to TipRanks: Willdan Group Insider Trading](https://www.tipranks.com/stocks/wldn/insider-trading)",
                "balancesheet": "[pos]As of March 31, 2025, Willdan Group's cash on hand was $38 million, with total liquidity of $88 million (including a $50 million undrawn line of credit). Free Cash Flow over the trailing 12 months was $40 million.[/pos] Total debt was $89.647 million as of April 4, 2025, with net debt at $49 million at the end of Q1 2025. [pos]The debt-to-equity ratio was a healthy 0.37 as of July 1, 2025.[/pos] [link to GuruFocus: Willdan Group Balance Sheet](https://www.gurufocus.com/term/roic/NASDAQ:WLDN) [link to BusinessWire: Willdan Group Expands Credit Facility](https://www.businesswire.com/news/home/20250501005000/en/Willdan-Group-Expands-Credit-Facility-to-200-Million)",
                "performance": "[pos]For the full year 2024, contract revenue increased by 10.9% to $565.8 million, and net revenue was up 9.9% to $296.3 million. Net income more than doubled to $22.6 million, and Adjusted EBITDA grew 24.2% to $56.8 million.[/pos] [pos]Q1 2025 showed continued strong growth with contract revenue up 24.4% to $152.4 million, net revenue up 23.8% to $85.3 million, net income up 59.3% to $4.7 million, and Adjusted EBITDA up 30.9% to $14.4 million.[/pos] [pos]The 2025 outlook projects net revenue between $320 million and $330 million, adjusted EBITDA between $63 million and $67 million, and adjusted EPS between $2.70 and $2.85 per share, indicating strong future prospects.[/pos] [link to Stock Titan: Willdan Group Q1 2025 Results](https://stocktitan.net/news/WLDN/willdan-group-reports-first-quarter-2025-financial-results-and-reaffirms-302138033.html)"
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
    update_wldn_description_with_highlights("D:\\users\\mukul\\SharedMukul\\Src\\forbes\\forbes-angular\\src\\assets\\data\\Americas_2025.json")
