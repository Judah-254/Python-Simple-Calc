# Base class
class Superhero:
    def __init__(self, name, power, strength_level):
        self.name = name
        self.power = power
        self.__strength_level = strength_level  # Encapsulated

    def introduce(self):
        print(f"I'm {self.name}, and my power is {self.power}!")

    def fight(self):
        print(f"{self.name} fights with strength level {self.__strength_level}.")

# Subclass showing inheritance and polymorphism
class FlyingHero(Superhero):
    def __init__(self, name, power, strength_level, flight_speed):
        super().__init__(name, power, strength_level)
        self.flight_speed = flight_speed

    # Overriding method (Polymorphism)
    def fight(self):
        print(f"{self.name} swoops in at {self.flight_speed} km/h and strikes!")

# Creating objects
hero1 = Superhero("Bolt", "Electric Shock", 85)
hero2 = FlyingHero("SkyBlazer", "Flight", 90, 300)

# Using methods
hero1.introduce()
hero1.fight()

hero2.introduce()
hero2.fight()
