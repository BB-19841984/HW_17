# Создайте класс Circle (окружность). Для данного класса реализуйте ряд перегруженных 
# операторов:
# Проверка на равенство радиусов двух окружностей (операция = =);
# Сравнения длин двух окружностей (операции >, <, <=,>=);
# Пропорциональное изменение размеров окружности, путем изменения ее радиуса 
# (операции + - += -=).

class Circle:
    def __init__(self, radius: int):
        self.radius = radius

    def circ_len(self):
        return self.radius*3.14*2
    def __eq__(self, other):
        return self.radius == other.radius
    def __lt__(self, other):
        return self.circ_len() < other.circ_len()
    def __le__(self, other): 
        return self.circ_len() <= other.circ_len()
    def __gt__(self, other):
        return self.circ_len() > other.circ_len()
    def __ge__(self, other): 
        return self.circ_len() >= other.circ_len()
    def __add__(self, num: int):
        return Circle(self.radius+num)
    def __iadd__(self, num: int): 
        self.radius += num
    def __sub__(self, num: int):
        return Circle(self.radius-num)
    def __isub__(self, num: int): 
        self.radius -= num


