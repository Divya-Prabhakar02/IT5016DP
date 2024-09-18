class Vehicle():
    def __init__(self):
        pass
    def move(self):
        print("The Vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("The Car is moving.")
gadi = Vehicle()
gadi.move()
gadi = Car()
gadi.move()