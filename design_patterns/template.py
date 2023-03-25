import dataclasses
import random
import string
from datetime import datetime
from enum import Enum


class VehicleFuelEnum(Enum):
    PETROL = "petrol"
    DIESEL = "diesel"


@dataclasses.dataclass
class Owner:
    first_name: str
    last_name: str
    full_name: str = dataclasses.field(init=False)

    def __post_init__(self):
        self.full_name = f"{self.first_name} {self.last_name}"

    @classmethod
    def take_input(cls):
        return cls(
            first_name=input("Owner First Name: "),
            last_name=input("Owner Last Name: "),
        )


@dataclasses.dataclass
class Vehicle:
    id: str = dataclasses.field(init=False, default_factory=str)
    name: str
    registeration_no: str = dataclasses.field(init=False, default_factory=str)
    registeration_date: datetime | None = dataclasses.field(init=False, default=None)
    owner: Owner
    fuel: VehicleFuelEnum

    @classmethod
    def take_input(cls):
        return cls(
            name=input("Vehicle Name: "),
            owner=Owner.take_input(),
            fuel=VehicleFuelEnum(input("Vehicle Fuel (petrol or diesel): ")),
        )


@dataclasses.dataclass
class VehicleRegistery:
    registered_vehicles: list[Vehicle] = dataclasses.field(default_factory=list)

    def _generate_vehicle_id(self, n: int = 10) -> str:
        return "".join(random.choices(string.ascii_lowercase, k=n))

    def _generate_vehicle_registeration_no(self, id: str) -> str:
        return f"{id[:2]}-{''.join(random.choices(string.ascii_uppercase, k=2))}-{''.join(random.choices(string.digits, k=4))}"

    def register(self, *vehicles: Vehicle):
        for vehicle in vehicles:
            vehicle.id = self._generate_vehicle_id()
            vehicle.registeration_no = self._generate_vehicle_registeration_no(
                vehicle.id
            )
            vehicle.registeration_date = datetime.now()
            self.registered_vehicles.append(vehicle)

        return vehicles


if __name__ == "__main__":
    registery = VehicleRegistery()

    while True:
        registery.register(Vehicle.take_input())
        print(registery.registered_vehicles, end="\n\n")
