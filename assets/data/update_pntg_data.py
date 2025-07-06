import json

def update_pntg_description_with_highlights(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for company in data:
        if company.get("TICKER") == "PNTG":
            company["DESCRIPTION"] = {
                "overview": "The Pennant Group, Inc. (NASDAQ: PNTG) is a holding company with independent operating subsidiaries that provide healthcare services, including home health, hospice, and senior living services, across 13 states. It operates on a decentralized model, empowering local leaders to manage their operations. [pos]The company recently announced a home health acquisition in Southern California on July 1, 2025, indicating continued growth through strategic acquisitions.[/pos] [link to Pennant Group News Release](https://investor.pennantgroup.com/news-releases/news-release-details/2025/The-Pennant-Group-Announces-Home-Health-Acquisition-in-Southern-California/default.aspx)",
                "insider_ownership": "[pos]Insider ownership is significant, with insiders owning 25.74% of the company.[/pos] This high level of insider ownership suggests that the interests of management are aligned with those of shareholders. [link to Simply Wall St PNTG Ownership](https://simplywall.st/stocks/us/healthcare/nasdaq-pntg/the-pennant-group/ownership)",
                "balancesheet": "The company uses a moderate amount of debt, primarily to fund acquisitions of smaller home health and hospice agencies as part of its growth strategy. [neg]As of March 31, 2025, the company reported total liabilities of $305.6 million and total debt of $180.5 million.[/neg] [link to Pennant Group Q1 2025 Earnings Release](https://investor.pennantgroup.com/news-releases/news-release-details/2025/The-Pennant-Group-Announces-First-Quarter-2025-Results/default.aspx)",
                "performance": "[pos]Pennant Group demonstrates strong returns on capital, with a Return on Invested Capital (ROIC) of 15.8% and a Return on Capital Employed (ROCE) of 18.2% for the trailing twelve months as of March 2025.[/pos] [link to AlphaSpread PNTG Financials](https://alphaspread.com/security/nasdaq/PNTG/profitability/roic)"
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
    update_pntg_description_with_highlights("D:\\users\\mukul\\SharedMukul\\Src\\forbes\\forbes-angular\\src\\assets\\data\\Americas_2025.json")