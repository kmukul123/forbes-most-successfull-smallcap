

import json

def update_vitl_description_with_links(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    for company in data:
        if company.get("TICKER") == "VITL":
            company["DESCRIPTION"] = {
                "overview": "Vital Farms is an ethical food company that markets and distributes pasture-raised food products, including eggs, butter, and ghee. It partners with a network of over 425 small family farms, emphasizing humane animal treatment and sustainable agriculture. The company has built a powerful brand centered on ethical practices and transparency, which resonates with a growing segment of consumers. [link to Vital Farms Q1 2025 Earnings Release](https://investors.vitalfarms.com/press-releases/press-release-details/2025/Vital-Farms-Reports-First-Quarter-2025-Financial-Results/default.aspx)",
                "insider_ownership": "[pos]Insider ownership is significant, at 18.75%[/pos]. [link to GuruFocus Vital Farms Insider Ownership](https://www.gurufocus.com/stock/VITL/insider)",
                "balancesheet": "[pos]Vital Farms has a strong balance sheet, with approximately $161.3 million in cash and no debt as of the first quarter of 2025.[/pos] [link to Vital Farms Q1 2025 Earnings Release](https://investors.vitalfarms.com/press-releases/press-release-details/2025/Vital-Farms-Reports-First-Quarter-2025-Financial-Results/default.aspx)",
                "performance": "[pos]Vital Farms demonstrates strong returns on capital, with a Return on Invested Capital (ROIC) of 37.17% and a Return on Capital Employed (ROCE) of 20.43%[/pos]. [link to GuruFocus Vital Farms ROIC/ROCE](https://www.gurufocus.com/stock/VITL/summary)"
            }
            break

    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    update_vitl_description_with_links("D:\\users\\mukul\\SharedMukul\\Src\\forbes\\forbes-angular\\src\\assets\\data\\Americas_2025.json")

