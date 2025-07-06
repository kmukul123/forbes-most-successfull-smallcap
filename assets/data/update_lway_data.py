import json

def update_lway_description_with_highlights(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for company in data:
        if company.get("TICKER") == "LWAY":
            company["DESCRIPTION"] = {
                "overview": "Lifeway Foods, Inc. manufactures probiotic and nutritious foods, primarily drinkable kefir. They also produce European-style soft cheeses and a ProBugs line for children. [pos]Lifeway Foods is headquartered in Morton Grove, Illinois, and employs 316 full-time employees, indicating a stable operational base.[/pos] [link to Lifeway Foods Investor Relations](https://lifewaykefir.com/investor-relations/)",
                "insider_ownership": "[pos]Insider ownership is significant, with Stock Titan reporting 66.68% as of July 1, 2025, suggesting strong alignment with shareholder interests.[/pos] [link to Stock Titan: Lifeway Foods Insider Trades](https://stocktitan.net/news/LWAY/lifeway-foods-inc-insider-trades-lway-stock-titan-66-68-insider-ownership-as-of-july-1-2025.html)",
                "balancesheet": "[pos]Lifeway Foods holds more cash than debt on its balance sheet and maintains a strong current ratio of 2.81.[/pos] The company has also modified its Loan and Security Agreement to increase its revolving loan commitment and extend its termination date, providing greater financial flexibility. [link to Investing.com: Lifeway Foods Q1 2025 Results](https://www.investing.com/news/stock-market-news/lifeway-foods-reports-strong-q1-2025-results-and-strategic-financial-moves-3460000)",
                "performance": "[pos]As of March 2025, Lifeway Foods' annualized Return on Invested Capital (ROIC) was 7.72%, with a TTM ROIC of 13.72%. Other historical data indicates a ROIC of 10.56% and a Return on Capital Employed (ROCE) of 15.35%, demonstrating solid profitability.[/pos] [link to GuruFocus: Lifeway Foods ROIC/ROCE](https://www.gurufocus.com/term/roic/NASDAQ:LWAY)"
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
    update_lway_description_with_highlights("D:\\users\\mukul\\SharedMukul\\Src\\forbes\\forbes-angular\\src\\assets\\data\\Americas_2025.json")
