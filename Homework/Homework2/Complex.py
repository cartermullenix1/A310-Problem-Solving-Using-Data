class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __str__(self):
        return str(self.real) + " + i * " + str(self.imag)
    
    def plus(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    
    def mult(self, other):
        return Complex(((self.real*other.real)-(self.imag*other.imag)),((self.real*other.imag)-(self.imag*other.real)))
    
    def __mul__(self, other):
        return Complex(((self.real*other.real)-(self.imag*other.imag)),((self.real*other.imag)-(self.imag*other.real)))
    
a = Complex(1,2)
b = Complex(2,3)

print(a+b)
print(a*b)


