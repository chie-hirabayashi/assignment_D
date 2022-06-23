class MyCounterV2:
    def __init__(self, value, step):
        self.value = value
        self.step = step

    def count_up(self):
        for n in range(1, self.step + 1):
            self.value += 1
        return self.value


counter1 = MyCounterV2(value=0, step=1)
counter2 = MyCounterV2(value=0, step=3)

print("<volue=0,step=1>")
print(counter1.value)
counter1.count_up()
print(counter1.value)
counter1.count_up()
print(counter1.value)
print(sep="")

print("<volue=0,step=3>")
print(counter2.value)
counter2.count_up()
print(counter2.value)
counter2.count_up()
print(counter2.value)
