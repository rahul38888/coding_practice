import enum
import random
import threading
from multiprocessing.pool import ThreadPool


class VehicleType(enum.Enum):
    CAR = 1
    BIKE = 2
    TRUCK = 3

    @staticmethod
    def from_value(val: int) -> "VehicleType":
        for vt in VehicleType:
            if vt.value == val:
                return vt
        return None


class Vehicle:
    def __init__(self, v_type: VehicleType, number: str):
        self.type = v_type
        self.number = number

    def __eq__(self, other):
        if type(other) is not Vehicle:
            return False
        return other.number == self.number

    def __hash__(self):
        return hash(self.number)

    def __str__(self):
        return f"{self.type.name}[number={self.number}]"


class Spot:
    def __init__(self, v_type: VehicleType, number: int):
        self.__type = v_type
        self.__vehicle: Vehicle = None
        self._number = number
        self.__lock = threading.Lock()

    def is_empty(self):
        with self.__lock:
            return self.__vehicle is None

    def park_vehicle(self, vehicle: Vehicle):
        if self.__type != vehicle.type or self.__vehicle:
            return False

        with self.__lock:
            if not self.__vehicle:
                self.__vehicle = vehicle
                return True
            return False

    def empty_spot(self):
        with self.__lock:
            self.__vehicle = None

    def has_vehicle(self, vehicle: Vehicle):
        with self.__lock:
            return self.__vehicle == vehicle

    def string(self):
        return self.__vehicle.type.name[0] if self.__vehicle else "_"


class Level:
    def __init__(self, level: int, spots_counts: dict[VehicleType, int]):
        self.__level = level
        self.__reverse_index: dict[Vehicle: Spot] = dict()
        spots: dict[VehicleType: list[Spot]] = dict()
        for t, c in spots_counts.items():
            if not spots.__contains__(t):
                spots[t] = []
            for i in range(c):
                spots[t].append(Spot(t, i))
        self.__spots_map = spots

    def park_vehicle(self, vehicle: Vehicle):
        if not self.__spots_map.__contains__(vehicle.type):
            return False

        for spot in self.__spots_map[vehicle.type]:
            if spot.is_empty() and spot.park_vehicle(vehicle):
                self.__reverse_index[vehicle] = spot
                return True
        return False

    def exit_vehicle(self, vehicle: Vehicle):
        if not self.__reverse_index.__contains__(vehicle):
            return False

        if self.__reverse_index.__contains__(vehicle):
            spot = self.__reverse_index[vehicle]
            spot.empty_spot()
            return True

        return False

    def display(self):
        tc = sum(list(map(lambda ss: len(ss), self.__spots_map.values())))
        print(f"Level: {self.__level}, total spots = {tc}")
        for spots in self.__spots_map.values():
            for spot in spots:
                print(spot.string(), end=" ")
        print()


class Singleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


class ParkingLot(metaclass=Singleton):
    def __init__(self, entries: int, exists: int):
        self.__entry_gates = ThreadPool(processes=entries)
        self.__exit_gates = ThreadPool(processes=exists)
        self.__levels: list[Level] = list()

    def add_level(self, spot_types: dict[VehicleType: int]):
        level = Level(len(self.__levels), spot_types)
        self.__levels.append(level)

    def __park_vehicle(self, vehicle: Vehicle):
        for level in self.__levels:
            if level.park_vehicle(vehicle):
                return True
        print(f"No spot available for {vehicle}")
        return False

    def __exit_vehicle(self, vehicle: Vehicle):
        for level in self.__levels:
            if level.exit_vehicle(vehicle):
                return True
        return False

    def vehicle_enter(self, vehicle: Vehicle):
        self.__entry_gates.apply(self.__park_vehicle, args=(vehicle, ))

    def vehicle_exit(self, vehicle: Vehicle):
        self.__exit_gates.apply(self.__exit_vehicle, args=(vehicle, ))

    def display(self):
        for level in self.__levels:
            level.display()


rd = random.Random(x=42)


def rand_string(seed: int):
    rd.seed(seed)
    return str(rd.randint(1000, 200000))


def rand_v_type(seed: int):
    rd.seed(seed)
    return VehicleType.from_value(rd.randint(1, 3))


if __name__ == '__main__':

    pl = ParkingLot(2, 2)
    pl.add_level(spot_types={VehicleType.CAR: 10, VehicleType.BIKE: 20, VehicleType.TRUCK: 10})
    pl.add_level(spot_types={VehicleType.CAR: 15, VehicleType.TRUCK: 10})
    pl.add_level(spot_types={VehicleType.CAR: 15, VehicleType.TRUCK: 10})

    v_count = 90
    queue = [Vehicle(rand_v_type(i), rand_string(i)) for i in range(v_count)]

    for vt in queue:
        pl.vehicle_enter(vt)

    pl.display()
