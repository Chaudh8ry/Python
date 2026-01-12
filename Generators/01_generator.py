def genLearn():
    yield "cup 1"
    yield "cup 2"
    yield "cup 3"

cups = genLearn()
# for cup in cups:
#     print(cup)

# next() : manually fetches the data
print(f"Manually using next(): {next(cups)}")