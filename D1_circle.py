class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return "%.2f" % (self.radius * self.radius * 3.14)

    def perimeter(self):
        return "%.2f" % (2 * self.radius * 3.14)


circle1 = Circle(1)
circle3 = Circle(3)

print("<半径1の円>")
print(circle1.area())
print(circle1.perimeter())
print(sep="")

print("<半径3の円>")
print(circle3.area())
print(circle3.perimeter())
