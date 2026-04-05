from models.vehicle.vehicle import Vehicle
from models.vehicle.vehicle_type import VehicleType
from models.vehicle.electric_vehicle import ElectricVehicle


class ElectricBike(Vehicle, ElectricVehicle):

    def __init__(self, reg_number: str, color: str, battery_percentage: float = 100):
        super().__init__(reg_number, color, VehicleType.ELECTRIC_BIKE)
        self.battery_percentage = battery_percentage

    def charge(self) -> None:
        print(f"{self.reg_number} is now charged with battery of {self.battery_percentage}%")

    def get_battery_percentage(self) -> float:
        return self.battery_percentage
