# Создайте класс Complex (комплексное число).
# Создайте перегруженные операторы для реализации арифметических операций для по 
# работе с комплексными числами (операции +, -, *, /).

class Complex:
 
    def __init__(self, a, b):
        self.a = a
        self.b = b
 
    def __repr__(self):
        return f'{self.a}{"-" if self.b < 0 else "+"}{abs(self.b)}j'
 
    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.a + other.a, self.b + other.b)
        if isinstance(other, (int, float)):
            return Complex(self.a + other, self.b)
        raise NotImplementedError
 
    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.a - other.a, self.b - other.b)
        if isinstance(other, (int, float)):
            return Complex(self.a - other, self.b)
        raise NotImplementedError
        
 
    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(self.a * other.a, self.b * other.b)
        if isinstance(other, (int, float)):
            return Complex(self.a * other, self.b)
        raise NotImplementedError
        
 
    def __truediv__(self, other):
        if isinstance(other, Complex):
            return Complex(self.a / other.a, self.b / other.b)
        if isinstance(other, (int, float)):
            return Complex(self.a / other, self.b)
        raise NotImplementedError
 
 
c1 = Complex(1, 2)
c2 = Complex(3, 4)
print(c1, c2)
print(c1 + c2)
print(c1 * c2)
print(c1 / c2)
