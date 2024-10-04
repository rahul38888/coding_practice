class LivingBeing:
    def __init__(self, name: str, age: int):
        """
        Encapsulates age and name
        """
        self.__name = name
        self.__age = age

    def age_by_years(self, years: int):
        """
            Provides only info it wants to
        """
        self.__age += years
        print(f"{self.__name} is now {self.__age} years old")

    def name(self) -> str:
        return self.__name


if __name__ == '__main__':
    """
    Age and name of Samantha is not accessible
    """
    lb = LivingBeing("Samantha", 16)
    lb.age_by_years(2)
