class Flat:

    def __init__(self, area, price):
        self.area = area
        self.price = price
    def __eq__(self, other):
        return self.area == other.area
    def __ne__(self, other):
        return self.area != other.area
    def __lt__(self, other):
        return self.price < other.price
    def __gt__(self, other):
        return self.price > other.price
    def __le__(self, other):
        return self.price <= other.price
    def __ge__(self, other):
        return self.price >= other.price

flat1 = Flat(400, 90000)
flat2 = Flat(120, 120000)
flat3 = Flat(390, 110000)

print(f"flat1 == flat2: {flat1 == flat2}")
print(f"flat1 != flat2: {flat1 != flat2}")
print(f"flat1 < flat2: {flat1 < flat2}")
print(f"flat1 > flat2: {flat1 > flat2}")
print(f"flat1 <= flat2: {flat1 <= flat2}")
print(f"flat1 >= flat2: {flat1 >= flat2}")
print(f"flat1 == flat3: {flat1 == flat3}")
print(f"flat1 != flat3: {flat1 != flat3}")
print(f"flat1 < flat3: {flat1 < flat3}")
print(f"flat1 > flat3: {flat1 > flat3}")
print(f"flat1 <= flat3: {flat1 <= flat3}")
print(f"flat1 >= flat3: {flat1 >= flat3}")