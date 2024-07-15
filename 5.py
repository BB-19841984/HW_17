from __future__ import annotations
 
 
class Roman:
    __map__ = (
        ('M', 1000),
        ('CM', 900),
        ('D', 500),
        ('CD', 400),
        ('C', 100),
        ('XC', 90),
        ('L', 50),
        ('XL', 40),
        ('X', 10),
        ('IX', 9),
        ('V', 5),
        ('IV', 4),
        ('I', 1)
    )
 
    def __init__(self, value: str):
        self.value = value
 
    def __add__(self, other: any) -> Roman:
        if isinstance(other, Roman):
            return Roman(self.to_roman(int(self) + int(other)))
        elif isinstance(other, int):
            return Roman(self.to_roman(int(self) + other))
        return NotImplemented
 
    def __sub__(self, other: any) -> Roman:
        if isinstance(other, Roman):
            return Roman(self.to_roman(int(self) - int(other)))
        elif isinstance(other, int):
            return Roman(self.to_roman(int(self) - other))
        return NotImplemented
 
    def __mul__(self, other: any) -> Roman:
        if isinstance(other, Roman):
            return Roman(self.to_roman(int(self) * int(other)))
        elif isinstance(other, int):
            return Roman(self.to_roman(int(self) * other))
        return NotImplemented
 
    def __div__(self, other: any) -> Roman:
        if isinstance(other, Roman):
            return Roman(self.to_roman(int(self) / int(other)))
        elif isinstance(other, int):
            return Roman(self.to_roman(int(self) / other))
        return NotImplemented
 
    def __str__(self) -> str:
        return self.value
 
    def __int__(self) -> int:
        return self.to_decimal(self.value)
 
    @classmethod
    def to_decimal(cls, value: str) -> int:
        if not value: return 0
        result, index = 0, 0
        for symbol, digit in cls.__map__:
            while value[index:index + len(symbol)] == symbol:
                result += digit
                index += len(symbol)
        return result
 
    @classmethod
    def to_roman(cls, value: int) -> str:
        if value == 0: return ""
        result = ""
        for symbol, digit in cls.__map__:
            while value >= digit:
                result += symbol
                value -= digit
        return result
