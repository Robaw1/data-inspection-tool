import pandas as pd
import matplotlib.pyplot as plt
import os
from src.data_inspector.validator import load_schema, validate_data

# 1. Load data and schema
df = pd.read_csv("data/dummy.csv")
schema = load_schema("configs/schema.yaml")

# 2. Run validation
errors = validate_data(df, schema)

# 3. Create the reports folder if it doesn't exist
os.makedirs("reports", exist_ok=True)

# 4. Generate the visualization using matplotlib
plt.figure(figsize=(8, 5))
df['age'].dropna().hist(bins=10, color='#4CAF50', edgecolor='black')
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.savefig("reports/age_distribution.png", bbox_inches='tight')
plt.close()

# 5. Generate the HTML report
error_items = "".join([f"<li style='color: #D8000C;'>{error}</li>" for error in errors])
if not error_items:
    error_items = "<li style='color: #4F8A10;'>All validation checks passed!</li>"

html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Data Quality Report</title>
    <style>
        body {{ font-family: -apple-system, sans-serif; max-width: 800px; margin: 40px auto; padding: 20px; }}
        .container {{ background: #f9f9f9; padding: 20px; border-radius: 8px; border: 1px solid #eee; }}
        img {{ max-width: 100%; border: 1px solid #ddd; border-radius: 4px; margin-top: 20px; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Data Quality Inspection Report</h1>
        <h2>Validation Results</h2>
        <ul>{error_items}</ul>
        <h2>Age Distribution Analysis</h2>
        <img src="age_distribution.png" alt="Age Distribution Histogram">
    </div>
</body>
</html>
"""

with open("reports/inspection_report.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("Pipeline complete! Check the 'reports' folder for your HTML report.")