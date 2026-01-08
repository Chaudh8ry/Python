staff = [("Vishal",17),("Ram",19),("Afaik",22)]

for name,age in staff:
    if(age>=18):
        print(f"{name} is eligible")
        # break
else:
    print("No one is eligible from the staff")