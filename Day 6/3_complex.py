# -----------------------Creating Complex Numbers----------------------
# using complex function
z1 = complex(3,4) # 3 + 4j
# directly specifying real and imaginary parts
z2 = 2 + 5j

# -----------------------Accessing Real and Imaginary Parts----------------------
print(z1.real) # accessing Real part (3)
print(z1.imag) # accessing Imaginary part (4)
print("\n")

# -----------------------Basic Arithemetic Operations----------------------
z3 = z1 + z2
z4 = z1 * z2
print(z3)
print(z4)

# -----------------------Conjugate----------------------
# a + bj => b + aj
z_conj = z1.conjugate() 
print(z_conj) # 4 + 3j

# -----------------------Absolute Value----------------------
# |z| = (a^2 + b^2)^1/2
print(abs(z1)) # (9 + 16)^1/2 --> (25)^1/2 --> 5 