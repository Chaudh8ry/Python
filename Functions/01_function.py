custOrder = [("Vishal","Chai-1"),("Arun","Chai-2"),("Afcon","Chai-3")]

def print_order(name,chai_type):
    print(f"{name} has ordered {chai_type}")

for customer,chai in custOrder:
    print_order(customer,chai)