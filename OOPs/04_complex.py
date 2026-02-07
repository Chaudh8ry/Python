# Creating our own ComplexNumber DataType
class ComplexNumber:
    def __init__(self, real = 0.0, imag = 0.0):
        # Initialize the complex number with real and imaginary parts
        self.real = real
        self.imag = imag

    # __str__ is a Magic Method, it automatically gets called when we print the object
    def __str__(self):
        # If real part is 0, only show imaginary part
        if self.real == 0:
            return f"({self.imag}j)"
        # If imaginary part is negative, format without '+'
        elif self.imag < 0:
            s = f"({self.real} {self.imag}i)"
        # Otherwise, show with '+' sign
        else:
            s = f"({self.real}+{self.imag}i)"
        return s

    # __add__ is a Magic Method for adding two ComplexNumber objects
    def __add__(self, other):
        # Add real parts
        realResult = self.real + other.real
        # Add imaginary parts
        imagResult = self.imag + other.imag
        # Return a new ComplexNumber object with the result
        ans = ComplexNumber(realResult, imagResult)
        return ans 
    
    # __sub__ is a Magic Method for subtracting two ComplexNumber objects
    def __sub__(self, other):
        # Subtract real parts
        realResult = self.real - other.real
        # Subtract imaginary parts
        imagResult = self.imag - other.imag
        # Return a new ComplexNumber object with the result
        ans = ComplexNumber(realResult, imagResult)
        return ans

    # __mul__ is a Magic Method for multiplying two ComplexNumber objects
    def __mul__(self,other):
        realResult = self.real * other.real - self.imag * other.imag
        imagResult = self.real * other.imag + other.real * self.imag
        ans = ComplexNumber(realResult,imagResult)
        return ans
    
    def __truediv__(self,other):
        den = other.real * other.real + other.imag * other.imag

        ans = self * ComplexNumber(other.real/den,(-1*other.imag)/den)
        return ans

    # Method to return the conjugate of the complex number
    def conjugate(self):
        # Conjugate is obtained by negating the imaginary part
        return ComplexNumber(self.real, -1 * self.imag)

cm1 = ComplexNumber(3,4)
cm2 = ComplexNumber(4,5)

print(cm1/cm2)

# print(cm1.conjugate())