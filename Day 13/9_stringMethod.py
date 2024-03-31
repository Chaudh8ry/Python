# Strings are Im-Mutable 
a = "VisHal"

# Here the original-existing string 'a' is not converted into uppercase first it is copied and then converted to Uppercase
print(a.upper())

# Lower Case
print(a.lower())

# 'rstrip()' removes trailing characters
b = "Hi Ji!!!!"
print(b.rstrip("!"))

# 'replace()' - as the name suggest
c = "Hello I am Harry, I run a YouTube channel CodeWithHarry"
print(c.replace("Harry","Vishal"))

# 'split()' - the split() method is a built-in string method used to split a string into a list of substrings based on a specified separator.
d = "Hello, World! This is a Sentence."
print(d.split()) # ['Hello,', 'World!', 'This', 'is', 'a', 'Sentence.']

email = "john.doe@example.com"
parts = email.split("@")  # Split by "@" symbol
print(parts)
# Output: ['john.doe', 'example.com']

# 'capitalize()' it converts the first letter of a string into Capital ,the rest other words of the string are turned to Lowercase
blogHeading = "hey Brother hOw are yoU?"
print(blogHeading.capitalize())

# 'center()' aligns the string at the centre
print(blogHeading.center(50)) # The length of blogHeading is 24 characters. The center(50) method centers the string within a string of length 50 by adding spaces on both sides. Since the original string is shorter than 50 characters, spaces will be added to make it centered.
print(len(blogHeading))
print(len(blogHeading.center(50)))

# 'count()' - frequency of something
print(blogHeading.count("e"))

# 'startswith()' opposite of endswith
# 'endswith()' it checks if a given string is ending with a given value. If yes then return True, else return False
x = "Hey Mike !!"
print(x.endswith("!"))
# we can also check for a value in between the string by providing start and end index positions
y = "Welcome to the console!"
print(y.endswith("to",4,10)) # to check if a specified substring "to" occurs at the end of the string. However, it applies the slicing indices (4, 10) to the string before performing the check.

# 'find()' this method searches for the first occurence of the given value and returns the index where it is present. If given value is absent from the string then return -1.
print(y.find("to"))

# 'index()' is similar to 'find' method the only difference is wehn the word is not present in the string it gives error instead of -1(like in 'find')

# 'isalnum()' returns True if our string is Alpha Numeric (contains only {A-Z},{a-z},{0-9}). No special characters/Symbols
print(y.isalnum())

# 'isalpha()' returns True onle of alphabets are present {A-Z},{a-z}

# 'islower()' returns True if all characters in string are in LowerCase
# 'isupper()' opposite of islower

# 'isprintable()' return True if string contains all printable characters ('\n' is one of the non-printable character)
u = "tu come manzanas" #TRUE
v = "tu come manzanas\n" #FALSE
print(u.isprintable())
print(v.isprintable())

# 'isspace()' returns True if string contains White spaces,else False

# 'istitle()' returns True if first letter of each word is Capital,else False

# 'swapcase()' changes charcater casing of a string. Uppercase to Lowercase and Vice-Versa

# 'title()' capitalizeseach letter of the word within the string
f = "f in the chat"
print(f.title())