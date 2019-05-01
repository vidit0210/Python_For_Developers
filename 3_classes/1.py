class Point:
    # Class Level Attributes
    default_color = 'red'

    @classmethod
    def zero(cls):
        return cls(0, 0)  # Point(0,0)

    @classmethod
    def ones(cls):
        return cls(1, 1)  # Point(1,1)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print('Points to be drawn are {} and {}'.format(self.x, self.y))


print(Point.default_color)
point_1 = Point(1, 2)
print(point_1.default_color)
Point.default_color = "yellow"
print(Point.default_color)
print(point_1.x)
print(point_1.draw())
point_0 = Point.zero()
print(point_0.draw())
