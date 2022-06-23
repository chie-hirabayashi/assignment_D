"""
D-1~3
"""


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * 3.14

    def perimeter(self):
        return 2 * self.radius * 3.14


circle1 = Circle(1)
circle2 = Circle(2)

print(circle2.radius)
print(circle1.area())
print(circle1.perimeter())


import math


class Rectangle:
    def __init__(self, height, width):
        self.height = float(height)
        self.width = float(width)

    def area(self):
        return self.height * self.width

    def diagonal(self):
        return math.sqrt((self.height) ** 2 + (self.width) ** 2)


rectangle1 = Rectangle(height=5, width=6)
rectangle2 = Rectangle(height=3, width=3)

print(rectangle1.height)
print(rectangle1.area())
print(rectangle1.diagonal())
print(rectangle2.area())
print(rectangle2.diagonal())
print(math.sqrt(2))


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return "%.2f" % self.side**2

    def diagonal(self):
        return "%.2f" % math.sqrt(((self.side) ** 2) * 2)


square1 = Square(side=1.5)
square2 = Square(side=15)


print(square1.area())
print(square1.diagonal())
print(square2.area())
print(square2.diagonal())

# 小数点以下2
n1 = 1.234567
n2 = 5
print(math.ceil(n1))  # 切り上げ
print(math.floor(n1))  # 切り下げ
print(round(n1))  # 四捨五入
print(round(n1, 2))  # 丸め
print(round(n2, 2))  # 丸め
print(f"{n1:.1f}")
print(f"{n2:.03f}")  # ゼロ埋め
print("%03d" % n1)
print("%.3f" % n1)

print("ーーーーーーーーーーーーーーーーー")

"""
D-5~6
"""
# takes no arguments///タイプミスに注意 init int とか


class MyCounterV1:
    def __init__(self, value):
        self.value = value

    def count_up(self):
        self.value += 1
        return self.value


counter1 = MyCounterV1(value=0)

print(counter1.value)
counter1.count_up()
print(counter1.value)


class MyCounterV2:
    def __init__(self, value, step):
        self.value = value
        self.step = step

    def count_up(self):
        for n in range(1, self.step + 1):
            self.value += 1
        return self.value


counter1 = MyCounterV2(value=0, step=5)

print(counter1.value)
counter1.count_up()
print(counter1.value)
counter1.count_up()
print(counter1.value)


class MyCounterV3:
    def __init__(self, value, step):
        self.value = value
        self.step = step

    def count_up(self):
        for n in range(1, self.step + 1):
            self.value += 1
        return self.value

    def count_down(self):
        for n in range(1, self.step + 1):
            self.value -= 1
        return self.value


counter1 = MyCounterV3(value=1, step=2)
counter2 = MyCounterV3(value=3, step=4)

print(counter1.value)

counter1.count_up()
print(counter1.value)

counter1.count_up()
print(counter1.value)

counter1.count_down()
print(counter1.value)


print(counter2.value)

counter2.count_down()
print(counter2.value)

counter2.count_down()
print(counter2.value)
