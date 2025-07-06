
import json

file_path = r"D:\users\mukul\SharedMukul\Src\forbes\forbes-angular\src\assets\data\Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if company["COMPANY"] == "Knowles":
        # Rename 'main' to 'overview'
        if "main" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["overview"] = company["DESCRIPTION"].pop("main")
        # Rename 'debt' to 'balancesheet'
        if "debt" in company["DESCRIPTION"]:
            company["DESCRIPTION"]["balancesheet"] = company["DESCRIPTION"].pop("debt")

        # Update overview with moat information and ROCE/ROIC
        company["DESCRIPTION"]["overview"] = """Knowles Corporation is a global supplier of advanced micro-acoustic, audio processing, and specialty component solutions. It is a leader in MEMS (micro-electro-mechanical systems) microphones, balanced armature speakers, and capacitors for markets like mobile, hearables, and IoT. [highlight]Knowles differentiates itself through its focus on niche markets, proprietary technologies, and innovative solutions in acoustics and audio processing. Its strategic shift towards higher-value medtech, defense, and AI-integrated products, along with strong R&D capabilities, contributes to its competitive moat.[/highlight] [pos]Knowles has a Return on Capital Employed (ROCE) of 6.37% and a Return on Invested Capital (ROIC) of 5.98% (GuruFocus, as of July 2025). Its ROCE was 5.1% as of September 2023, underperforming the Electronic industry average.[/pos] [link to Knowles Investor Relations](https://www.knowles.com/investors) [link to StockAnalysis KN ROIC/ROCE](https://stockanalysis.com/stocks/kn/roic/) [link to GuruFocus KN ROIC](https://www.gurufocus.com/term/roic/NYSE:KN)"""

        # Update insider_ownership
        company["DESCRIPTION"]["insider_ownership"] = """[pos]Insider ownership is modest, with TipRanks reporting 2.49% and GuruFocus reporting 3.58%. Insiders have both bought and sold shares recently.[/pos] [link to TipRanks KN Ownership](https://www.tipranks.com/stocks/kn/ownership) [link to GuruFocus KN Ownership](https://www.gurufocus.com/term/insider_ownership/NYSE:KN)"""

        # Update balancesheet with cash levels and debt details, and stock dilutions/buybacks
        company["DESCRIPTION"]["balancesheet"] = """The company manages a moderate level of debt, which provides the financial flexibility to invest in R&D and manufacturing capacity. [pos]As of March 2025, Knowles reported $101.90 million in cash and cash equivalents, with total debt of $209.80 million, resulting in a net cash position of -$107.90 million. Its debt-to-equity ratio is 0.28. The company has an active stock repurchase program, with an additional $150 million authorized in February 2025, bringing the total available to $194 million. Annual share buybacks were $53.7 million in 2024. Shareholders have not experienced meaningful dilution in the past year.[/pos] [link to Knowles Q1 2025 Earnings Release](https://www.knowles.com/news-releases/news-release-details/2025/Knowles-Corporation-Reports-First-Quarter-2025-Financial-Results/default.aspx) [link to Simply Wall St KN Financials](https://simplywall.st/stocks/us/technology/nyse-kn/knowles/financials)"""

        # Ensure scalability is present and updated
        if "scalability" not in company["DESCRIPTION"]:
            company["DESCRIPTION"]["scalability"] = ""
        company["DESCRIPTION"]["scalability"] = """Scalable by winning design slots in high-volume consumer electronics like smartphones, earbuds, and smart speakers. Growth is driven by the increasing number of audio components per device and the demand for higher-performance audio."""

        break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Knowles entry updated successfully.")
