import json

def update_mlr_description_with_highlights(file_path):
    print(f"Attempting to update: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print("File read successfully.")

        found_mlr = False
        for company in data:
            if company.get("TICKER") == "MLR":
                print("Found MLR entry. Updating description...")
                company["DESCRIPTION"] = {
                    "overview": "Miller Industries is the world's largest manufacturer of towing and recovery equipment. It produces a wide range of vehicles, from small wreckers to heavy-duty industrial carriers, under various brand names like Century, Vulcan, and Holmes. The company's competitive advantage is built on its market leadership, strong brand recognition, and extensive distribution network. [link to Miller Industries Investor Relations](https://www.millerind.com/investors)",
                    "insider_ownership": "Insider holdings at Miller Industries are approximately 2.22% as of July 2025. [link to TipRanks MLR Insider Trading](https://www.tipranks.com/stocks/mlr/insider-trading)",
                    "balancesheet": "As of the first quarter of 2025, Miller Industries reported $27.4 million in cash and cash equivalents and $75.50 million in total debt. The company repurchased approximately $2.1 million of its shares during the first quarter. [link to Miller Industries Q1 2025 Financial Results](https://www.prnewswire.com/news-releases/miller-industries-reports-2025-first-quarter-results-302138033.html)",
                    "performance": "[pos]Miller Industries has demonstrated solid profitability, with a Return on Invested Capital (ROIC) of 13.19% for the trailing twelve months.[/pos] The company's Return on Equity (ROE) was 14.19% and its Return on Capital Employed (ROCE) was 14.96%. [link to GuruFocus MLR ROIC data](https://www.gurufocus.com/term/roic/NYSE:MLR)"
                }
                # Rename keys as requested
                if "main" in company["DESCRIPTION"]:
                    company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
                if "debt" in company["DESCRIPTION"]:
                    company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")
                found_mlr = True
                print("MLR description updated in memory.")
                break

        if not found_mlr:
            print("MLR entry not found in data.")

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print("File written successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    update_mlr_description_with_highlights("D:\\users\\mukul\\SharedMukul\\Src\\forbes\\forbes-angular\\src\\assets\\data\\Americas_2025.json")