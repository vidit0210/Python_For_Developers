class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def createRandom(cls):
        return cls(1, 2)

    def __str__(self):
        return '{} and {}'.format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point.createRandom()
point2 = Point(11, 12)
point3 = Point.createRandom()
print(point)
print(point == point3)
print(point2 > point)
print(point + point3)
