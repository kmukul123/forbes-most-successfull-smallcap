

import json

def update_uti_description_with_highlights(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for company in data:
        if company.get("TICKER") == "UTI":
            company["DESCRIPTION"] = {
                "overview": "Universal Technical Institute, Inc. (NYSE: UTI) provides education programs in transportation, skilled trades, and healthcare. They operate 15 campuses across 9 states under brands such as UTI, MIAT College of Technology, Motorcycle Mechanics Institute, Marine Mechanics Institute, and NASCAR Technical Institute. They also include Concorde Career Colleges, which operates across 17 campuses in 8 states, offering programs in Allied Health, Dental, Nursing, Patient Care, and Diagnostic fields. [link to Universal Technical Institute Investor Relations](https://investor.uti.edu)",
                "insider_ownership": "Insider ownership is relatively low, with the company being primarily owned by institutional investors.",
                "balancesheet": "The company manages a moderate level of debt, often related to campus facilities and strategic acquisitions of other vocational schools.",
                "performance": "[pos]For fiscal year 2025 second-quarter results (reported May 7, 2025), revenues increased by 12.6% to $207.4 million and net income increased to $11.4 million.[/pos] [link to Universal Technical Institute Q2 2025 Results](https://www.prnewswire.com/news-releases/universal-technical-institute-inc-reports-fiscal-year-2025-second-quarter-results-302138033.html)"
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
    update_uti_description_with_highlights("D:\\users\\mukul\\SharedMukul\\Src\\forbes\\forbes-angular\\src\\assets\\data\\Americas_2025.json")

