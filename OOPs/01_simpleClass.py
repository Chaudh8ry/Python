class chai:
    pass 

class chaiTime:
    pass

print(type(chai)) #<class 'type'> ,chai is a class

ginger_tea = chai()
print(type(ginger_tea)) #<class '__main__.chai'> , ginger_tea is a instance of chai
print(type(ginger_tea) is chai) #true
print(type(ginger_tea) is chaiTime)#false