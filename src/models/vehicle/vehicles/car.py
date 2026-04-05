from models.vehicle.vehicle import Vehicle
from models.vehicle.vehicle_type import VehicleType


class Car(Vehicle):

    def __init__(self, reg_number: str, color: str):
        super().__init__(reg_number, color, VehicleType.CAR)
