class MyCounterV1:
    def __init__(self, value):
        self.value = value

    def count_up(self):
        self.value += 1
        return self.value


counter1 = MyCounterV1(value=0)
counter2 = MyCounterV1(value=7)

print("<volue=0>")
print(counter1.value)
counter1.count_up()
print(counter1.value)
counter1.count_up()
print(counter1.value)
print(sep="")

print("<volue=7>")
print(counter2.value)
counter2.count_up()
print(counter2.value)
counter2.count_up()
print(counter2.value)
