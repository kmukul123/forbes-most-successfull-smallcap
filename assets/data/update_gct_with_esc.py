

import json

def escape_json_string(value):
    """Escapes a string for use in JSON."""
    return json.dumps(value)[1:-1]

# Load the existing data
with open('D:/users/mukul/SharedMukul/Src/forbes/forbes-angular/src/assets/data/Americas_2025.json', 'r') as f:
    try:
        data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        # Attempt to fix the JSON by reading as text and removing the most common error
        f.seek(0)
        file_content = f.read()
        # A simple and common fix is to remove trailing commas before '}'
        import re
        file_content = re.sub(r',\s*([}\]])', r'\1', file_content)
        try:
            data = json.loads(file_content)
            print("Successfully repaired JSON data.")
        except json.JSONDecodeError as e:
            print(f"Could not automatically repair JSON: {e}")
            exit(1)


# Find the entry for GigaCloud Technology
for company in data:
    if company['COMPANY'] == 'GigaCloud Technology':
        # Update the description
        company['DESCRIPTION'] = {
            "overview": escape_json_string("GigaCloud Technology operates a global business-to-business (B2B) e-commerce marketplace for large parcel merchandise, such as furniture and home appliances. It connects manufacturers, primarily in Asia, with resellers in the U.S. and Europe, providing a complete solution from sourcing to payment and logistics. [highlight]The company's marketplace GMV increased 56.1% year-over-year to $1,416.7 million for the 12 months ended March 31, 2025.[/highlight] The company's competitive advantage, or \"moat\", is built on a combination of factors that create a powerful network effect. The company's B2B marketplace seamlessly integrates product discovery, payment processing, and a complete logistics solution, which is particularly crucial for the large and bulky items it specializes in. This integrated platform creates high switching costs for both buyers and sellers who become accustomed to the efficiency of the ecosystem. [link to GigaCloud Technology Announces First Quarter 2025 Financial Results](https://investors.gigacloudtech.com/news-releases/news-release-details/gigacloud-technology-announces-first-quarter-2025-financial)"),
            "insider_ownership": escape_json_string("[pos]Insider ownership is substantial, with insiders owning about 16-30% of the company.[/pos] CEO Lei Wu holds a 23% stake. [link to TipRanks GCT Insider Trading](https://www.tipranks.com/stocks/gct/insider-trading)"),
            "balancesheet": escape_json_string("As of March 31, 2025, GigaCloud had total liabilities of $678.1 million. The company has a share repurchase program of $78 million and has already repurchased $61.8 million worth of shares. [link to GigaCloud Technology Announces First Quarter 2025 Financial Results](https://investors.gigacloudtech.com/news-releases/news-release-details/gigacloud-technology-announces-first-quarter-2025-financial)"),
            "performance": escape_json_string("[pos]The company demonstrates strong returns on capital, with a Return on Invested Capital (ROIC) of 17.41% for the trailing twelve months (TTM) as of March 2025.[/pos] This exceeds its weighted average cost of capital (WACC) of 6.24%, indicating value creation. [link to GuruFocus GCT ROIC data](https://www.gurufocus.com/term/roic/NASDAQ:GCT)")
        }
        break

# Write the updated data back to the file
with open('D:/users/mukul/SharedMukul/Src/forbes/forbes-angular/src/assets/data/Americas_2025.json', 'w') as f:
    json.dump(data, f, indent=4)

print("GigaCloud Technology data updated successfully.")
