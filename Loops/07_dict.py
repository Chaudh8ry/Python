# List of users with their purchase details
users = [
    {"name": "Vishal", "id": 1, "total": 100, "coupon": "P20"},
    {"name": "Vishal", "id": 2, "total": 120, "coupon": "F10"},
    {"name": "Vishal", "id": 3, "total": 80, "coupon": "P50"},
]

# Dictionary mapping coupon codes to discount rules
# Each coupon has a tuple: (percentage_discount, fixed_discount)
discounts = {
    "P20": (0.2, 0),   # 20% discount
    "F10": (0.5, 0),   # 50% discount
    "P50": (0, 10),    # Flat ₹10 discount
}

# Loop through each user in the list
for user in users:
    # Get the discount rule for the user's coupon
    # If coupon not found, default to (0,0) meaning no discount
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    
    # Calculate discount amount:
    # (percentage of total) + (fixed discount)
    discount_amount = user["total"] * percent + fixed
    
    # Print the result in a readable format
    print(f'{user["name"]} paid {user["total"]} and got a Discount of rupees {discount_amount}')
