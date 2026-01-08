def calculate_bill(cups, price_per_cup):
    total = cups * price_per_cup
    return total

my_bill = calculate_bill(3,12)
print(f"Total bill {my_bill}")