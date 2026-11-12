#1)I would use .get() when looking up optioanl data that might be missing, like a phone number or secondary email, so the program does not crash. I would use bracket notation when a field is required, like a customer ID or price, so the program immediately catches missing critical data.
#2)This reminds me of adding up totals by category in Excel, like using a SUMIF formula or a Pivot Table. Python is better for huge lists of data because it adds everything up automaticaly.
# EXERCISE 1: One customer
print("--- Exercise 1 ---")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 450.00
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)
print()

# EXRCISE 2: Update and add
print("--- Exercise 2 ---")
customer["phone"] = "555-0199"
print("After adding phone:", customer)

customer["tier"] = "platinum"
print("After updating tier:", customer)

del customer["email"]
print("After deleting email:", customer)
print()

# EXERCISE 3: Safe lookup
print("--- Exercise 3 ---")
email_lookup = customer.get("email", "no email on file")
print("Using .get():", email_lookup)

try:
    print(customer["email"])
except KeyError:
    print("KeyError caught! Bracket notation crashed because 'email' was deleted.")
print()

# EXCERCISE 4: Iterate
print("--- Exercise 4 ---")
for key, value in customer.items():
    print(f"{key}: {value}")

# Iterating without .items() (e.g., `for x in customer:`) only loops through 
# the dictionary's keys, not the values.
print()

# EXERCISE 5: Lookup table
print("--- Exercise 5 ---")
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

current_tier = customer["tier"]
discount_rate = tier_discounts.get(current_tier, 0)
purchase_amount = 200
final_price = purchase_amount - (purchase_amount * discount_rate)

print(f"Tier: {current_tier} | Discount: {int(discount_rate * 100)}% | Final Price: ${final_price:.2f}")
print()

# EXERCISE 6: List of dicts
print("--- Exercise 6 ---")
customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "silver"},
    {"name": "Charlie", "tier": "gold"}
]

for person in customers:
    p_name = person["name"]
    p_tier = person["tier"]
    rate = tier_discounts.get(p_tier, 0)
    discount_amount = 300 * rate
    print(f"{p_name} ({p_tier}) receives a ${discount_amount:.2f} discount on a $300 purchase.")
print()

# EXERCISE 7: Nested catalog
print("--- Exercise 7 ---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for item_name, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK alert: {item_name} only has {details['stock']} left!")
print()

# EXERCISE 8: Sales by region
print("--- Exercise 8 ---")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

region_totals = {}

for tx in transactions:
    reg = tx["region"]
    amt = tx["amount"]
    region_totals[reg] = region_totals.get(reg, 0) + amt

for reg in sorted(region_totals):
    print(f"{reg}: {region_totals[reg]}")
