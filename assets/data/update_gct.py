import json

def update_gct_description(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    for company in data:
        if company.get("TICKER") == "GCT":
            company["DESCRIPTION"] = {
                "overview": "GigaCloud Technology operates a global business-to-business (B2B) e-commerce marketplace for large parcel merchandise, such as furniture and home appliances. It connects manufacturers, primarily in Asia, with resellers in the U.S. and Europe, providing a complete solution from sourcing to payment and logistics. [highlight]The company's marketplace GMV increased 56.1% year-over-year to $1,416.7 million for the 12 months ended March 31, 2025.[/highlight] The company's competitive advantage, or \"moat\", is built on a combination of factors that create a powerful network effect. The company's B2B marketplace seamlessly integrates product discovery, payment processing, and a complete logistics solution, which is particularly crucial for the large and bulky items it specializes in. This integrated platform creates high switching costs for both buyers and sellers who become accustomed to the efficiency of the ecosystem. [link to GigaCloud Technology Announces First Quarter 2025 Financial Results](https://investors.gigacloudtech.com/news-releases/news-release-details/gigacloud-technology-announces-first-quarter-2025-financial)",
                "insider_ownership": "[pos]Insider ownership is substantial, with insiders owning about 16-30% of the company.[/pos] CEO Lei Wu holds a 23% stake. [link to TipRanks GCT Insider Trading](https://www.tipranks.com/stocks/gct/insider-trading)",
                "balancesheet": "As of March 31, 2025, GigaCloud had total liabilities of $678.1 million. The company has a share repurchase program of $78 million and has already repurchased $61.8 million worth of shares. [link to GigaCloud Technology Announces First Quarter 2025 Financial Results](https://investors.gigacloudtech.com/news-releases/news-release-details/gigacloud-technology-announces-first-quarter-2025-financial)",
                "performance": "[pos]The company demonstrates strong returns on capital, with a Return on Invested Capital (ROIC) of 17.41% for the trailing twelve months (TTM) as of March 2025.[/pos] This exceeds its weighted average cost of capital (WACC) of 6.24%, indicating value creation. [link to GuruFocus GCT ROIC data](https://www.gurufocus.com/term/roic/NASDAQ:GCT)"
            }
            break

    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    update_gct_description("D:\\users\\mukul\\SharedMukul\\Src\\forbes\\forbes-angular\\src\\assets\\data\\Americas_2025.json")