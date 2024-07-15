# Вам необходимо создать класс Airplane (самолет). 
# С помощью перегрузки операторов реализовать: 
# Проверка на равенство типов самолетов (операция = =); 
# Увеличение и уменьшение пассажиров в салоне самолета (операции + - += -=);
# Сравнение двух самолетов по максимально возможному количеству пассажиров на 
# борту (операции > < <= >=).

class Airplane:
    def __init__(self, aircraft_type, current_passengers, max_passengers):
        self.aircraft_type = aircraft_type
        self.current_passengers = current_passengers
        self.max_passengers = max_passengers

    def __eq__(self, other):
        return self.aircraft_type == other.aircraft_type

    def __iadd__(self, passengers):
        self.current_passengers = passengers
        return self

    def __isub__(self, passengers):
        self.current_passengers = passengers
        return self

    def __lt__(self, other):
        return self.max_passengers < other.max_passengers
    
    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __eq__(self, other):
        return self.max_passengers == other.max_passengers


plane1 = Airplane("Боинг", 1000, 1500)
plane2 = Airplane("Аэробус", 1500, 2000)

if plane1 == plane2:
    print("Типы самолетов равны")
else:
    print("Типы самолетов разные")


plane1+=50
plane2-=25


if plane1 < plane2:
    print("Количество пассажиров на борту первого самолета меньше")
elif plane1 > plane2:
    print("Количество пассажиров на борту первого самолета больше")
else:
    print("Количество пассажиров на борту обоих самолетов одинаковое")