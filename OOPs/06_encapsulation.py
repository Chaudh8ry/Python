class Students:
    __numberOfStudents = 0
    __schhoolName = "VBBS"

    def __init__(self,name,rollNumber,marks):
        self.name = name
        self.rollNumber = rollNumber
        # private attribute (encapsulated) -> cannot be accessed directly outside the class
        self.__marks = marks
        self.numberOfStudents = Students.__numberOfStudents + 1
        Students.__numberOfStudents = Students.__numberOfStudents + 1

    # getter method -> provides controlled access to private data (__marks)
    def getMarks(self):
        return self.__marks
    
    # setter method -> allows controlled modification of private data (__marks)
    def setMarks(self,newMarks,passCode):
        # Only update marks if correct passCode is given
        if(passCode == self.__auth()):
            self.__marks = newMarks
        else:
            return "Bhaag Yaha se"  # Unauthorized access message

    #  private method for auth   
    def __auth(self):
        return "0000"
    
# Creating an object of Students
s1 = Students("Vishal",33,79)

# Using setter to update marks (encapsulation ensures only valid updates happen)
s1.setMarks(45,"0000")

# Using getter to access marks (direct access to __marks is not allowed)
print(s1.getMarks())