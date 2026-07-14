# Customer list (name, balance)
customers = [
    ("Eftu", 1200),
    ("Sara", 800),
    ("Dawit", 300),
    ("Abel", 1500),
    ("Hana", 450)
]

# Function to determine customer tier
def tier(balance):
    if balance >= 1000:
        return "Premium"
    elif balance >= 500:
        return "Standard"
    else:
        return "Basic"



# Display customer information
print("Customer Report")
print("-" * 30)

for name, balance in customers:
    customer_tier = tier(balance)

    print(f"Name: {name}")
    print(f"Balance: {balance}")
    print(f"Tier: {customer_tier}")
    print()

    if customer_tier == "Premium":
        premium += 1
    elif customer_tier == "Standard":
        standard += 1
    else:
        basic += 1

# Summary
print("Summary")
print("-" * 30)
print("Premium Customers:", premium)
print("Standard Customers:", standard)
print("Basic Customers:", basic)