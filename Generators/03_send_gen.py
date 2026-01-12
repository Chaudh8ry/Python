def chai_customer():
    print("Welcome! What chai would you like?")
    order = yield #The generator pauses here and waits to receive a value from the outside via .send(value). That value gets assigned to order.
    while True:
        print(f"Preparing: {order}") #Uses the last received order to print what’s being prepared.
        order = yield #Pauses again, waiting for the next order sent via .send(value). That new value replaces order, and the loop continues

stall = chai_customer() #generator object created

next(stall) 
# Starts the generator. It runs until the first yield.

# Prints: Welcome! What chai would you like?

# Pauses at order = yield, waiting for a value to be sent.

# This step is called priming the generator—you must do it before .send() the first time, otherwise Python doesn’t know where to deliver the value.

stall.send("Masala Chai")
# Sends "Masala Chai" into the paused order = yield.

# Assigns order = "Masala Chai"
stall.send("Lemon Chai")