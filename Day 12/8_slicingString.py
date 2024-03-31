a = "apple"
print("Number of Characters in Apple are",len(a))

# String slicing is a powerful technique that allows you to extract specific portions of a string, creating new substrings from the original
b = "Banana"
# including '0' but not '7'
print(b[0:7]) #Banana
print(b[2:7]) #nana
print(b[0:6]) #Banan

# Negative-Slicing
print(b[0:-3]) #Ban
# this work as print(b [0 : len(b) - 3 ] )

print(b[-3:-1]) # an 
# ( b [len(b) - 3 : len(b) - 1]) --> (b [3:5])


nm = "harry"
print(nm[-4:-2])
"""
nm="Harry"
print(nm[-4:-2])
The length of the string is 5, and the order of characters starts from zero, so H(0), a(1), r(2), r(3), y(4). 
Back to the code;
(len(nm)-4-->5-4=1
(len(nm)-4-->5-2=3
Hypothetically new statement is print(nm[1:3])
we know the starting point is 1, but to access the character's order we use n-1 principle.
 So, order of character=n-1
OC=3-1=2
Take the order of characters from 1 to 2 from the actual string; hence, the output is (ar).
"""