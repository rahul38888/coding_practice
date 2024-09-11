from abc import abstractmethod, ABC
from math import pi


class Shape(ABC):
    @abstractmethod
    def volume(self) -> float:
        pass


class Cube(Shape):
    def __init__(self, length: int, width: int, height: int):
        self.length = length
        self.width = width
        self.height = height

    def volume(self) -> float:
        return self.length * self.width * self.height


class Sphere(Shape):
    def __init__(self, radius: int):
        self.radius = radius

    def volume(self) -> float:
        return 4 * pi * self.radius * self.radius * self.radius/3


if __name__ == '__main__':
    shapes: list[Shape] = [Cube(1,1,1),
                           Sphere(1)]
    for shape in shapes:
        print(f"Volume of {type(shape).__name__} is {shape.volume()}")
