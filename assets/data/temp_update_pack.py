
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Ranpak Holdings":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Ranpak is a leading provider of environmentally sustainable, paper-based packaging solutions for e-commerce and industrial supply chains. It provides a full system of protective packaging materials and the machines that process them. [pos]Ranpak Holdings has a Return on Capital Employed (ROCE) of -0.51% and a Return on Invested Capital (ROIC) of -0.34% (StockAnalysis). Its 5-year average ROIC was 1.1%.[/pos] [link to Ranpak Holdings Investor Relations](https://www.ranpak.com/investors/) [link to StockAnalysis PACK ROIC/ROCE](https://stockanalysis.com/stocks/pack/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Primarily owned by private equity and institutional investors. Insider ownership varies across sources, from 6.83% (GuruFocus) to 9.66% (TipRanks).[/pos] [link to GuruFocus PACK Ownership](https://www.gurufocus.com/term/insider_ownership/NYSE:PACK) [link to TipRanks PACK Ownership](https://www.tipranks.com/stocks/pack/ownership)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company carries a significant debt load, which was used to finance its acquisition by a private equity firm and subsequent investments. [pos]As of March 31, 2025, Ranpak Holdings reported a cash balance of $65.5 million, with $409.0 million outstanding under its USD-denominated first lien term facility. As of December 31, 2024, total debt was $415.7 million.[/pos] [neg]Ranpak Holdings has experienced stock dilution, with a notable increase in weighted average shares outstanding from Q1 2024 to Q1 2025. While a $50 million share repurchase program was authorized in July 2022, no shares have been repurchased under this program as of May 2025.[/neg] [link to Ranpak Holdings Q1 2025 Earnings Release](https://www.ranpak.com/news-releases/news-release-details/2025/Ranpak-Holdings-Corp.-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to Ranpak Holdings Share Repurchase Program](https://www.ranpak.com/news-releases/news-release-details/2022/Ranpak-Holdings-Corp.-Announces-Share-Repurchase-Program/default.aspx)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Highly scalable 'razor-and-blade' model. It places packaging machines (the 'razor') at customer sites and then sells the proprietary paper consumables (the 'blades'). Growth is driven by the expansion of e-commerce and the corporate push for sustainable packaging."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Ranpak Holdings entry updated successfully.")
