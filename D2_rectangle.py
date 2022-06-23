import math


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return "%.2f" % (self.height * self.width)

    def diagonal(self):
        return "%.2f" % (math.sqrt((self.height) ** 2 + (self.width) ** 2))


rectangle1 = Rectangle(height=5, width=6)
rectangle2 = Rectangle(height=3, width=3)

print("<5*6の長方形>")
print(rectangle1.area())
print(rectangle1.diagonal())
print(sep="")

print("<3*3の長方形>")
print(rectangle2.area())
print(rectangle2.diagonal())
