import json

def update_gct_description_with_highlights(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for company in data:
        if company.get("TICKER") == "GCT":
            company["DESCRIPTION"] = {
                "overview": "GigaCloud Technology operates a global business-to-business (B2B) e-commerce marketplace for large parcel merchandise, such as furniture and home appliances. It connects manufacturers, primarily in Asia, with resellers in the U.S. and Europe. [pos]The company's marketplace GMV increased 56.1% year-over-year to $1,416.7 million for the 12 months ended March 31, 2025.[/pos] The company's moat is its integrated platform combining product discovery, payment, and logistics, creating high switching costs. [link to GigaCloud Technology Announces First Quarter 2025 Financial Results](https://investors.gigacloudtech.com/news-releases/news-release-details/gigacloud-technology-announces-first-quarter-2025-financial)",
                "insider_ownership": "[pos]Insider ownership is substantial, with CEO Lei Wu holding a 23% stake.[/pos] This aligns leadership with shareholder interests. [link to TipRanks GCT Insider Trading](https://www.tipranks.com/stocks/gct/insider-trading)",
                "balancesheet": "[neg]As of March 31, 2025, GigaCloud had total liabilities of $678.1 million, a significant figure for a potential acquirer.[/neg] [pos]The company has an active share repurchase program of $78 million and has already repurchased $61.8 million worth of shares.[/pos] [link to GigaCloud Technology Announces First Quarter 2025 Financial Results](https://investors.gigacloudtech.com/news-releases/news-release-details/gigacloud-technology-announces-first-quarter-2025-financial)",
                "performance": "[pos]The company demonstrates strong value creation with a Return on Invested Capital (ROIC) of 17.41% for the TTM as of March 2025, which exceeds its WACC of 6.24%.[/pos] [link to GuruFocus GCT ROIC data](https://www.gurufocus.com/term/roic/NASDAQ:GCT)"
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
    update_gct_description_with_highlights("D:\\users\\mukul\\SharedMukul\\Src\\forbes\\forbes-angular\\src\\assets\\data\\Americas_2025.json")
