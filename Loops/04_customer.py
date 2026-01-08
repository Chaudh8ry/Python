# zip() is a built‑in function that combines elements from multiple iterables (like lists, tuples, or strings) into pairs (or tuples) based on their position.

names = ["Vishal", "Alex", "Ilia","Conor"]
rollNo = [33,34,35,36]

for name, roll in zip(names,rollNo):
    print(f"{name} has class Roll no. {roll}")