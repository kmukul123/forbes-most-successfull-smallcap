

import json

def update_clmb_description_with_highlights(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for company in data:
        if company.get("TICKER") == "CLMB":
            company["DESCRIPTION"] = {
                "overview": "Climb Global Solutions is a value-added global IT distribution and solutions company specializing in emerging and innovative technologies. They operate through multiple business units across the U.S., Canada, and Europe, focusing on connecting innovative technology vendors with resellers and managed service providers. [pos]The company emphasizes growth through acquisition, having completed its fifth accretive acquisition in 2024.[/pos] [link to Climb Global Solutions Investor Relations](https://www.climbglobalsolutions.com/investors/)",
                "insider_ownership": "Insider ownership is around 10%, with a strong presence from its board and executive team, aligning their interests with shareholders.",
                "balancesheet": "[pos]As of March 31, 2025, cash and cash equivalents were $32.5 million, with $0.6 million of outstanding debt and no borrowings under its $50 million revolving credit facility.[/pos] [link to Climb Global Solutions Q1 2025 Financial Results](https://www.globenewswire.com/news-release/2025/05/01/835000/0/en/Climb-Global-Solutions-Reports-First-Quarter-2025-Financial-Results.html)",
                "performance": "[pos]Net sales increased 49% to $138.0 million in Q1 2025 compared to Q1 2024. Net income rose 35% to $3.7 million, or $0.81 per diluted share. Adjusted EBITDA increased 38% to $7.6 million.[/pos] A quarterly dividend of $0.17 per share was declared payable on May 16, 2025. [link to Climb Global Solutions Q1 2025 Financial Results](https://www.globenewswire.com/news-release/2025/05/01/835000/0/en/Climb-Global-Solutions-Reports-First-Quarter-2025-Financial-Results.html)"
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
    update_clmb_description_with_highlights("D:\\users\\mukul\\SharedMukul\\Src\\forbes\\forbes-angular\\src\\assets\\data\\Americas_2025.json")

