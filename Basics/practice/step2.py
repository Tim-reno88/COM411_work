class Cat:
    def __init__(self, make, power, engine_size):
        self.make = make
        self.power = power
        self.engine_size = engine_size

    def modify(self):
        self.power += 20

    def fix(self):
        self.engine_size += 1

        if self.power >= 1:
            print("bhp gains")
        else:
            print("we need to get more bhp")


car1 = Cat("Ford", 4, 4)
car2 = Cat("Dodge", 1, 2)
car3 = Cat("Old Tom", 10, 6)

car1.modify()
car2.modify()
car3.modify()
print(car1.make)
print(car1.power)
print(car1.engine_size)

car1 = Cat("Ford", 4, 4)
car2 = Cat("Dodge", 1, 2)
car3 = Cat("Old Tom", 10, 6)

car1.power()
car2.power()
car3.power()
print(car1.engine_size)
print(car2.engine_size)
print(car3.engine_size)