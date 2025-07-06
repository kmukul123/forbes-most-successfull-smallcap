

import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Clearpoint Neuro":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """ClearPoint Neuro is a medical device company that provides a navigation platform for minimally invasive neurosurgeries. Its ClearPoint system enables the real-time, MRI-guided placement of catheters, electrodes, and drug delivery cannulas in the brain. [highlight]Clearpoint Neuro's competitive moat is built on high switching costs (due to co-labeling with therapeutic agents), proprietary technology and IP (ClearPoint system, SmartFlow cannula, patents), niche market leadership (only FDA-approved direct MRI-guided stereotactic system), a \"razor-and-blade\" business model, and strategic partnerships with biologics/pharmaceutical companies.[/highlight] [pos]Clearpoint Neuro has a Return on Invested Capital (ROIC) of -37.71% and a Return on Capital Employed (ROCE) of -93.49% (StockAnalysis).[/pos] [link to Clearpoint Neuro Investor Relations](https://ir.clearpointneuro.com/) [link to StockAnalysis CLPT ROIC/ROCE](https://stockanalysis.com/stocks/clpt/roic/)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership is significant, with 26.91% (WallStreetZen) of the company owned by insiders. Bruce C. Conway is the largest individual shareholder (14.29%). CEO Joseph M. Burnett recently purchased shares through an ESPP. Insiders have been net selling recently.[/pos] [link to WallStreetZen CLPT Ownership](https://www.wallstreetzen.com/stocks/us/medical-devices/nasdaq-clpt/clearpoint-neuro/ownership) [link to Stock Titan CLPT Insider Trading](https://stocktitan.net/news/CLPT/clearpoint-neuro-inc-insider-trades-clpt-stock-titan-26-91-insider-ownership-as-of-july-1-2025.html)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """Funds its operations and R&D through a combination of equity financing and strategic partnership revenue, operating with a manageable debt load. [pos]As of March 31, 2025, Clearpoint Neuro reported $12.4 million in cash and cash equivalents. Total debt was $3.44 million. The company has significantly reduced its debt from a debt-to-equity ratio of 608% five years ago to being largely debt-free at certain points.[/pos] [neg]However, the company has experienced stock dilution, with a registered direct offering in May 2025 where Oberland Capital purchased 275,808 shares, generating over $3.5 million in gross proceeds.[/neg] [link to Clearpoint Neuro Q1 2025 Earnings Release](https://ir.clearpointneuro.com/news-releases/news-release-details/2025/ClearPoint-Neuro-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to Clearpoint Neuro Registered Direct Offering](https://ir.clearpointneuro.com/news-releases/news-release-details/2025/ClearPoint-Neuro-Announces-Registered-Direct-Offering-of-Common-Stock/default.aspx)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Highly scalable 'razor-and-blade' model. It sells the reusable hardware and software (the 'razor') and generates recurring revenue from the sale of single-use disposable products (the 'blades') for each procedure. Growth is driven by the expanding field of gene and cell therapy for neurological disorders."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Clearpoint Neuro entry updated successfully.")

