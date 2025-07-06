import json

def update_vitl_description(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    for company in data:
        if company.get("TICKER") == "VITL":
            company["DESCRIPTION"] = {
                "overview": "Vital Farms is an ethical food company that markets and distributes pasture-raised food products, including eggs, butter, and ghee. It partners with a network of over 425 small family farms, emphasizing humane animal treatment and sustainable agriculture. The company has built a powerful brand centered on ethical practices and transparency, which resonates with a growing segment of consumers.",
                "insider_ownership": "[pos]Insider ownership is significant, with insiders owning between 19% and 30% of the company.[/pos] This high level of insider ownership suggests that the interests of management are aligned with those of shareholders.",
                "balancesheet": "[pos]Vital Farms has a strong balance sheet, with approximately $161.3 million in cash and no debt as of the first quarter of 2025.[/pos] This provides the company with considerable flexibility for future growth and investments.",
                "performance": "[pos]Vital Farms demonstrates strong returns on capital, with a Return on Invested Capital (ROIC) of around 14% and a Return on Capital Employed (ROCE) in the range of 15% to 20%.[/pos] These figures suggest that the company is effectively generating profits from its capital investments."
            }
            break

    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    update_vitl_description("D:\\users\\mukul\\SharedMukul\\Src\\forbes\\forbes-angular\\src\\assets\\data\\Americas_2025.json")