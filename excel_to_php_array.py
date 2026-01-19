import pandas as pd

# Change this to your actual Excel file path
excel_file = 'Haier_warranty.xlsx'

# Read Excel sheet (assumes first sheet)
df = pd.read_excel(excel_file)

# Show columns (optional, for debug)
print("Excel Columns:", df.columns.tolist())

# Fix column names to match yours exactly, or rename them here:
# For example:
# df.rename(columns={'Warranty nbr': 'WarrantyNbr', 'Model nbr': 'ModelNbr', 'Issue date': 'IssueDate'}, inplace=True)

# Convert Issue date to YYYY-MM-DD string
df['Issue date'] = pd.to_datetime(df['Issue date']).dt.strftime('%Y-%m-%d')

# Hardcode brand here (edit as needed)
brand = 'HAIER'

# Build PHP array string
php_lines = []
php_lines.append("$warranty_data = array(")

for index, row in df.iterrows():
    warranty_number = str(row['Warranty nbr']).strip().split('.')[0]  # remove decimals if any
    model = str(row['Model nbr']).strip()
    issue_date = row['Issue date']

    # Build PHP entry
    entry = f"  '{warranty_number}' => array("
    entry += f"\n    'brand' => '{brand}',"
    entry += f"\n    'model' => '{model}',"
    entry += f"\n    'issueDate' => '{issue_date}'"
    entry += "\n  ),"
    php_lines.append(entry)

php_lines.append(");")

# Join all lines
php_code = "\n".join(php_lines)

# Save to file or print
with open('warranty_data.php', 'w') as f:
    f.write(php_code)

print("PHP warranty array code saved to 'warranty_data.php'")
