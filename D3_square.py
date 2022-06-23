import math


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return "%.2f" % self.side**2

    def diagonal(self):
        return "%.2f" % math.sqrt(((self.side) ** 2) * 2)


square1 = Square(side=1.5)
square2 = Square(side=15)


print("<1.5の正方形>")
print(square1.area())
print(square1.diagonal())
print(sep="")

print("<15の正方形>")
print(square2.area())
print(square2.diagonal())
