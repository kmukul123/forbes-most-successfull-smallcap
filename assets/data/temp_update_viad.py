import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Viad":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information
        company["DESCRIPTION"]["overview"] = """Viad Corp operates as an attractions and hospitality company under the brand Pursuit, and a marketing and events company under the brand GES. Pursuit offers travel experiences in iconic locations (e.g., Banff, Jasper, Alaska), while GES provides services for live events and exhibitions. [highlight]Pursuit's competitive moat is built on its unique portfolio of experiential travel and hospitality assets in iconic, high-barrier-to-entry locations, offering integrated experiential offerings and leveraging a strategic 'Refresh, Build, Buy' growth strategy.[/highlight]"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[neg]Insider ownership is relatively low, with Stock Titan reporting approximately 2.93% as of July 2025.[/neg] [link to Stock Titan PRSU Ownership](https://stocktitan.net/news/PRSU/viad-corp-insider-trades-prsu-stock-titan-2-93-insider-ownership-as-of-july-1-2025.html)"""

        # Update balancesheet with cash levels and debt details
        company["DESCRIPTION"]["balancesheet"] = """The company carries a significant amount of debt, used to finance the acquisition and development of its high-value hospitality assets and attractions. [pos]As of March 31, 2025, Viad reported cash and cash equivalents of $22.8 million.[/pos] [neg]Total debt stood at $78.9 million as of March 31, 2025.[/neg] [link to Pursuit Collection Q1 2025 Financial Results](https://www.pursuitcollection.com/news/pursuit-announces-first-quarter-2025-financial-results)"""

        # Update stock dilutions/buybacks
        company["DESCRIPTION"]["stock_dilutions_buybacks"] = """[neg]The company has experienced stock dilutions, with diluted weighted-average outstanding common shares increasing by 33.7% in Q1 2025 compared to Q1 2024.[/neg] [pos]Viad has authorized share repurchase programs, with 440,540 shares remaining available for repurchase as of December 31, 2017, and a long-standing plan that has repurchased over 10 million shares for $227.32 million.[/pos] [link to Pursuit Collection Q1 2025 Financial Results](https://www.pursuitcollection.com/news/pursuit-announces-first-quarter-2025-financial-results) [link to Simply Wall St PRSU Dilution](https://simplywall.st/stocks/us/commercial-professional-services/nyse-prsu/viad/news/is-viad-nyseprsu-s-share-price-momentum-driven-by-its-financial)"""

        # Update ROCE/ROIC
        company["DESCRIPTION"]["roic_roce"] = """[neg]As of June 8, 2025, Pursuit Attractions and Hospitality's Return on Invested Capital (ROIC) is 0.23% (TTM).[/neg] [link to Investing.com PRSU ROIC](https://www.investing.com/equities/viad-corp-roic)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """The Pursuit hospitality segment is highly scalable through its 'Refresh, Build, Buy' strategy, acquiring and developing new attractions in iconic destinations. The GES segment's scalability is tied to the health of the global trade show and live events industry."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Viad entry updated successfully.")