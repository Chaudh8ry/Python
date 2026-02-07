class chaiOrder:
    def __init__(self,type_,size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size}ml of {self.type} chai"
    
order1 = chaiOrder("Masala",120)
print(order1.summary())
order2 = chaiOrder("Lemon",150)
print(order2.summary())