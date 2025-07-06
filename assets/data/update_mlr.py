import json

def update_mlr_description(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    for company in data:
        if company.get("TICKER") == "MLR":
            company["DESCRIPTION"] = {
                "overview": "Miller Industries is the world's largest manufacturer of towing and recovery equipment. It produces a wide range of vehicles, from small wreckers to heavy-duty industrial carriers, under various brand names like Century, Vulcan, and Holmes. The company's competitive advantage is built on its market leadership, strong brand recognition, and extensive distribution network. [link to Miller Industries Investor Relations](https://www.millerind.com/investors)",
                "insider_ownership": "Insider holdings at Miller Industries are relatively low, at approximately 1.68% as of June 2025. [link to KappaSignal insider ownership data](https://kappasignal.com/insider-holdings/1073829/mlr-miller-industries-inc)",
                "balancesheet": "As of the first quarter of 2025, Miller Industries reported $27.4 million in cash and cash equivalents and $75.50 million in total debt. The company has a share repurchase program of $25.0 million. [link to Miller Industries financial statements](https://stockanalysis.com/stocks/mlr/financials/)",
                "performance": "[pos]Miller Industries has demonstrated solid profitability, with a Return on Invested Capital (ROIC) of 13.19% for the trailing twelve months.[/pos] The company's Return on Equity (ROE) was 14.19% and its Return on Capital Employed (ROCE) was 14.96%. [link to GuruFocus MLR ROIC data](https://www.gurufocus.com/term/roic/NYSE:MLR)"
            }
            break

    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    update_mlr_description("D:\\users\\mukul\\SharedMukul\\Src\\forbes\\forbes-angular\\src\\assets\\data\\Americas_2025.json")