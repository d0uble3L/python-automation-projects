import json

def calculate_annual_spending(json_file):
    # Read the JSON file
    with open(json_file, 'r') as file:
        bills = json.load(file)
    
    # Calculate monthly and annual spending
    monthly_total = sum(bills.values())
    annual_total = monthly_total * 12
    
    return monthly_total, annual_total

# File path to the JSON file
json_file = 'bills.json'

# Calculate spending
monthly_total, annual_total = calculate_annual_spending(json_file)

# Print results
print(f"Monthly Total Spending: ${monthly_total:.2f}")
print(f"Annual Total Spending: ${annual_total:.2f}")
