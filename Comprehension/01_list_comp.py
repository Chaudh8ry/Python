# [expression for item in iterable if condition]
squares = [x**2 for x in range(10)]
print("Square: ",squares)


chaiMenu = [
    "Masala Chai",
    "Iced Lemon Chai",
    "Green Chai",
    "Iced Peach Chai",
    "Ginger Chai"
]

#Filtering with "Iced" 
iced_tea = [my_tea for my_tea in chaiMenu if "Iced" in my_tea]
print(f"{iced_tea}")
# ['Iced Lemon Chai', 'Iced Peach Chai']

# LONG CODE using Loop
# iced_tea = []
# for my_tea in chaiMenu:
#     if "Iced" in my_tea:
#         iced_tea.append(my_tea)

lenTea = [my_tea for my_tea in chaiMenu if len(my_tea)<13]
print(f"{lenTea}")
# ['Masala Chai', 'Green Chai', 'Ginger Chai']