
import json

file_path = "D:/users/mukul/SharedMukul/Src/forbes/forbes-angular/src/assets/data/Americas_2025.json"

with open(file_path, 'r') as f:
    data = json.load(f)

for company in data:
    if "DESCRIPTION" in company:
        description = company["DESCRIPTION"]
        if "overview" in description:
            if "performance" in description:
                description["overview"] += " " + description["performance"]
                del description["performance"]
            if "moat" in description:
                description["overview"] += " " + description["moat"]
                del description["moat"]

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)
