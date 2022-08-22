class Vehical():
    def __init__(self, bs):
        self.bs=bs

    def drive(self, speed):
        self.mode="driving"
        self.speed=speed

class Car(Vehical):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.wheels=4
        self.doors=4
        self.enginetype=enginetype

    def drive(self, speed):
        super().drive(speed)
        print("driving my ", self.enginetype, "at", self.speed)


class Motorcycle(Vehical):
    def __init__(self, enginetype, sidecar):
        super().__init__("Motorcycle")
        if sidecar:
            self.wheels=3
        else:
            self.wheels=2
        self.doors=0
        self.enginetype=enginetype

car1 = Car("gas")
car2 = Car("electric")
mc1 = Motorcycle("gas", True)

print(mc1.wheels)
print(car1.enginetype)
print(car2.doors)

car1.drive(30)
car2.drive(70)