import enum
from multiprocessing.pool import ThreadPool
from typing import Union


class VehicleType(enum.Enum):
    CAR = 1
    BIKE = 2
    TRUCK = 3


class Vehicle:
    def __init__(self, v_type: VehicleType):
        self.type = v_type


class Spot:
    def __init__(self, v_type: VehicleType):
        self.__type = v_type
        self.__filled = False
        self.__vehicle = None
        self.__address = ""

    def is_empty(self):
        return not self.__filled

    def put_vehicle(self, vehicle: Vehicle):
        if self.__type != vehicle.type:
            return False
        self.__vehicle = vehicle
        self.__filled = True

    def empty_spot(self):
        self.__vehicle = None
        self.__filled = False


class Singleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


class ParkingLot(metaclass=Singleton):
    def __init__(self, entries: int, exists: int, spots_counts: dict[VehicleType, int]):
        self.__entries = entries
        self.__exists = exists
        self.__entry_gates = ThreadPool(processes=entries)
        self.__exit_gates = ThreadPool(processes=exists)
        self.__reverse_index = dict()
        spots = dict()
        for t, c in spots_counts.items():
            if not spots.__contains__(t):
                spots[t] = []
            for i in range(c):
                spots[t].append(Spot(t))
        self.__spots_map = spots

    def __get_empty_splot(self, vehicle: Vehicle) -> Union[Spot, None]:
        if self.__spots_map.__contains__(vehicle.type):
            raise NotImplementedError(f"No spots for vehicle type {vehicle.type}")

        spots = self.__spots_map[vehicle.type]

        for spot in spots:
            if spot.is_empty():
                return spot

        return None

    def __fill_an_empty_spot(self, vehicle: Vehicle):
        spot = self.__get_empty_splot(vehicle)
        if spot:
            spot.put_vehicle(vehicle)

    def vehicle_enter(self):
        pass


if __name__ == '__main__':
    pl = ParkingLot(2, 2, {VehicleType.CAR: 40, VehicleType.BIKE: 50, VehicleType.TRUCK: 10})
