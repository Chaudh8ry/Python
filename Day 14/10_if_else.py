age = int(input("Enter Your Age: "))

# Unlike many other programming languages where braces {} are used to denote code blocks, Python uses indentation to indicate the beginning and end of blocks of code.
if(age<18):
    print("You Can not Drive") #left side space (indentation) is important in python, If we remove space here the program will show error. This indentation indicates that these lines of code belong to their respective conditional blocks.
else: 
    print("You Can Drive")
print("No Indentation") # This line is executed regardless of the age. This line is not associated with else