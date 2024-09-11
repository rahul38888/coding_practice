from src.writeupcode.LLD.OOP.encapsulation import LivingBeing


class Animal(LivingBeing):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def eat(self, food: str) -> bool:
        raise NotImplementedError("Should be implemented by subclass")


class Cat(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def eat(self, food: str):
        return food == "fish"


class Dog(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def eat(self, food: str):
        return food == "bone"


if __name__ == '__main__':
    """
    Animal a generic class can take many forms (Cat, Dog) due to polymorphism
    Each form can implement its methods
    """
    pets: list[Animal] = [Cat("Newton", 2),
                          Dog("Einstein", 1)]
    for pet in pets:
        if pet.eat("bone"):
            print(f"{pet.name()} have eaten bone")
        else:
            print(f"{pet.name()} don't like eating bone")
