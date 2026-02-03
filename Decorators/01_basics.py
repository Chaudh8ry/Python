import time
# Creating a Decorator
def time_deck(base_fn):
    def enhanced_fn():
        start_time = time.time()
        base_fn()
        end_time = time.time()
        print(f"Task time: {end_time - start_time} seconds")
    return enhanced_fn

@time_deck #majorly used syntax
def brew_tea():
    print("Brewing tea...")
    time.sleep(1) #wait for 1sec.
    print("Tea is ready!")

# Method - 1
# dec_brew_tea = time_deck(brew_tea) #passing base function to decorator NOTE: dont pass brew_tea(), it will trigger brew_tea fn. call 
# dec_brew_tea()

#Method - 2
#using @timer_dec above base function
brew_tea()

@time_deck #reusing decorators
def make_match():
    print("Making matcha...")
    time.sleep(1)
    print("Matcha is ready")

make_match()