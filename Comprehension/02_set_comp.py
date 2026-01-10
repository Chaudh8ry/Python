# Similar to list comprehension but creates a set (unique values).
favourite_chais = [
    "Masala Chai","Green Chai","Masala Chai",
    "Lemon Tea","Green Chai","Elaichi Chai"
]

unique_chai = {chai for chai in favourite_chais}
print(f"Unique chais: {unique_chai}")

recipes = {
    "Masala Chai": ["ginger","cardamom","clove"],
    "Elaichi Chai": ["cardamom","milk"],
    "Spicy Chai": ["ginger","black pepper","clove"]
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
print(f"unique spices: {unique_spices}")

# Step 1: Outer loop
# for ingredients in recipes.values()
# Iterates over each list of spices (like ["ginger","cardamom","clove"]).

# Step 2: Inner loop
# for spice in ingredients
# Iterates over each spice inside that list.

# Step 3: Expression
# spice
# Collects each spice encountered.

# Step 4: Set braces { ... }
# Because we used {}, the result is a set (unique values, no duplicates).

# 🧾 Execution Flow
# First tea → "Masala Chai" → spices: "ginger","cardamom","clove" → add them.
# Second tea → "Elaichi Chai" → spices: "cardamom","milk" → "cardamom" already exists, "milk" is new.
# Third tea → "Spicy Chai" → spices: "ginger","black pepper","clove" → "ginger" and "clove" already exist, "black pepper" is new.