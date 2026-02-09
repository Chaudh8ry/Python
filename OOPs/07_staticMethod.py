class Students:
    __numberOfStudents = 0
    __schhoolName = "VBBS" # Private class variable storing school name

    def __init__(self,name,rollNumber,marks):
        self.name = name
        self.rollNumber = rollNumber
        self.__marks = marks
        self.numberOfStudents = Students.__numberOfStudents + 1
        Students.__numberOfStudents = Students.__numberOfStudents + 1

    def getMarks(self):
        return self.__marks
    
    def setMarks(self,newMarks,passCode):
        if(passCode == self.__auth()):
            self.__marks = newMarks
        else:
            return "Bhaag Yaha se"  
        
    def __auth(self):
        return "0000"
    
    # A static method in Python is a method that belongs to the class but does not depend on any instance (self). 
    # It can be called directly using the class name without creating an object.
    @staticmethod 
    def getSchoolName(): # getter
        # Static method: Accesses school name without needing an object
        return Students.__schhoolName
    
    @staticmethod
    def setSchoolName(newSchoolName ): # setter
        Students.__schhoolName = newSchoolName


    def getStudentsSchoolName(self):
        # Instance method: Accesses the same school name but requires an object
        return Students.__schhoolName

# --- Usage and Output --- 
Students.setSchoolName("NSIT")


print(Students.getSchoolName()) 
# ✅ Works: static method can be called directly on the class 
# Output: VBBS 

# print(Students.getStudentsSchoolName()) 
# ❌ Error: instance method requires an object, but none is provided 
# Output: TypeError: getStudentsSchoolName() missing 1 required positional argument: 'self' 
s1 = Students("Varun",45,90) 
s2 = Students("arun",25,40) 

print(s1.getStudentsSchoolName()) 
# ✅ Works: called via object s1, returns school name 
# Output: VBBS 

print(s2.getSchoolName()) 
# ✅ Works: called via object s2, returns school name 
# Output: VBBS