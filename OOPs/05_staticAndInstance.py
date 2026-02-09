class Student:
    # static (class-level) property: shared by All Instances of Students
    numberOfStudents = 0
    schoolName = "VBBS"

    def __init__(self,name,rollNuumber,marks):
        # Instance variables: unique to each object
        self.name = name
        self.rollNumber = rollNuumber
        self.marks = marks

        # This line creates an instance variable 'numberOfStudents' for THIS object
        # It take the current class-level value and adds 1
        self.numberOfStudents = Student.numberOfStudents + 1

        # This line updates the class-level (static) property itself
        Student.numberOfStudents = Student.numberOfStudents + 1

s1 = Student("Vishal",33,78)
s2 = Student("David",13,82)

print(s1.numberOfStudents)
print(s2.numberOfStudents)