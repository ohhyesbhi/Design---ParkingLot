from abc import ABC
from models.vehicle.vehicle_type import VehicleType


class Vehicle(ABC):

    def __init__(self, reg_number: str, color: str, vehicle_type: VehicleType):
        self.reg_number = reg_number
        self.color = color
        self.vehicle_type = vehicle_type

    def __repr__(self):
        return f"{self.vehicle_type.value}(reg={self.reg_number}, color={self.color})"
