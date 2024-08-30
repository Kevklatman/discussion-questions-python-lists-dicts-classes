# Finish the implementation of the Car class so it has the functionality described below


class Car:

    all = []

    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car.all.append(self)

    def drive(self):
        print("VROOOOOOOOOOOOM!")

    @classmethod
    def brake(cls):
        print("SCREEEECH!")


volvo_lightning = Car("Volvo", "Lightning")
yugo = Car("Zastava", "Yugo")
lada = Car("AvtoVAZ", "Lada")

volvo_lightning.make
# => "Volvo"
volvo_lightning.model
# => "Lightning"

yugo.drive()
# => "VROOOOOOOOOOOOM!"

print(Car.all)
# => [<__main__.Car object at 0x1049247c0>, <__main__.Car object at 0x1049247c8>, <__main__.Car object at 0x1049247d6>]

# BONUS:

Car.brake()
# => "SCREEEECH!"

volvo_lightning = Car(make="Volvo", model="Lightning")

volvo_lightning.make
# => "Volvo"
volvo_lightning.model
# => "Lightning"
