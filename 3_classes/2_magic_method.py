class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '{} and {}'.format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    @classmethod
    def zeros(cls):
        return cls(0, 0)


point1 = Point(1, 2)
point2 = Point(10, 20)
print(point1 == point2)
print(point2 > point1)
