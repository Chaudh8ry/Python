def infiniteGen():
    count = 1
    while True: #running infinite rule
        yield f"refil no.{count}"
        count+=1
    
#Creating generator Object
refill = infiniteGen()

#controlling the loop range
for _ in range(5):
    print(next(refill))