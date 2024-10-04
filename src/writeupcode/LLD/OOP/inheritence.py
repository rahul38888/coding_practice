from src.writeupcode.LLD.OOP.encapsulation import LivingBeing
from src.writeupcode.LLD.OOP.exceptions import NotAllowed


class Human(LivingBeing):
    def __init__(self, name: str, age: int, money: int):
        """
        Human inherits LivingBeing properties and method and defines its own
        """
        super().__init__(name, age)
        self.__money = money

    def spend(self, money: int, on: str):
        if money > self.__money:
            raise NotAllowed(f"Not enough money to spend on {on}")
        self.__money -= money
        print(f"You have spent {money} Rupees on {on}")

    def age_by_years(self, years: int):
        """
        Super class method can be overriden
        """
        super().age_by_years(years)
        tax = 10 * years
        try:
            self.spend(tax, "taxes")
        except NotAllowed as e:
            self.spend(min(tax, self.__money), "taxes")
            print("Warning not enough money to pay taxes")
        else:
            print("Unknown exception")
        finally:
            print("Done with transaction")


if __name__ == '__main__':
    """
    Override methods will have different behaviour
    """
    ron = Human("Ron", 22, 100)
    ron.age_by_years(5)
    ron.spend(35, "food")
