import time
def time_dec(base_fn):
    def enhanced_fn(*args,**kwargs):
        start_time = time.time()
        base_fn(*args,**kwargs)
        end_time = time.time()
        print(f"Task time: {end_time - start_time}")
    return enhanced_fn

@time_dec
def brew_tea(tea_type,delayTime):
    print(f"Brew {tea_type}...")
    time.sleep(delayTime)
    print(f"{tea_type} is ready!")

@time_dec
def brew_matcha(matcha_type,delayTime):
    print(f"Brew {matcha_type}...")
    time.sleep(delayTime)
    print(f"{matcha_type} is ready!")

brew_tea("Lemon Tea",1)
brew_matcha(matcha_type="Creatine Monohydrate",delayTime=2)