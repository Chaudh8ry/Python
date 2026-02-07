class ChaiCup:
    size = 150

    def describe(self):
        return f"A {self.size}ml chai cup is Ready"
    
cup = ChaiCup()
print(cup.describe())