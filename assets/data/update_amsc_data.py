import json

def update_amsc_description_with_highlights(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for company in data:
        if company.get("TICKER") == "AMSC":
            company["DESCRIPTION"] = {
                "overview": "American Superconductor provides technologies and services to the energy sector, offering solutions for the power grid (voltage regulation, resilient electric grid systems) and designs for wind turbines. [pos]Their proprietary superconductor technology offers a significant competitive advantage for large-scale projects, aligning with the global push for clean energy and grid modernization.[/pos] [link to Willdan Group Investor Relations](https://www.willdangroup.com/)",
                "insider_ownership": "[pos]Insider ownership is substantial, with WallStreetZen reporting 39.81% and key individuals holding significant stakes, indicating strong alignment with shareholder interests.[/pos] [link to WallStreetZen: American Superconductor Insider Ownership](https://www.wallstreetzen.com/stocks/us/nasdaq/amsc/insider-trading)",
                "balancesheet": "[pos]As of March 31, 2025, cash on hand was $38 million. Total debt was $89.647 million as of April 4, 2025, with net debt at $49 million. The debt-to-equity ratio was a healthy 0.37 as of July 1, 2025, indicating manageable leverage.[/pos] [link to GuruFocus: Willdan Group Balance Sheet](https://www.gurufocus.com/term/roic/NASDAQ:WLDN)",
                "performance": "[neg]ROIC was reported as 2.66% (StockAnalysis) or 0.03 (Fintel), and ROCE was 3.51%, which are relatively low figures.[/neg] [pos]However, the five-year average ROIC was negative 29.1%, indicating recent improvements in capital efficiency. Q3 2025 ROI was 1.81%.[/pos] [link to StockAnalysis: American Superconductor ROIC](https://stockanalysis.com/stocks/amsc/roic/) [link to Fintel: American Superconductor ROIC](https://fintel.io/n/us/amsc) [link to CSI Market: American Superconductor ROI](https://csimarket.com/stocks/single_return.php?code=AMSC&return=ROI)"
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
    update_amsc_description_with_highlights("D:\\users\\mukul\\SharedMukul\\Src\\forbes\\forbes-angular\\src\\assets\\data\\Americas_2025.json")
