# instead of writing a loop to yield values from another iterable, you can just use yield from. Its a generator delegation system (lets one generator pass cintrol to another)
def generator1():
    yield from [1,2,3]

def generator2():
    yield from generator1()
    yield from [4,5,6]

ans = generator2() #created this generator object so i can close the geneartor later

for val in ans:
    print(val) # 1,2,3,4,5,6

ans.close() #closes the generator and free up the memory space