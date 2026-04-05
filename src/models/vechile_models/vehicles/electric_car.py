
from models.vechile_models.vehicle import Vehicle
from enums.vehicle_type import VehicleType
from models.vechile_models.electric_vechicle import ElectricChargeSupportedVehicle

class ElectricCar(Vehicle, ElectricChargeSupportedVehicle):

    def __init__(self, reg_number: str, color: str, battery_percentage: float = 100):
        super().__init__(reg_number, color, VehicleType.ELECTRIC_CAR)
        self.battery_percentage = battery_percentage
       
    def charge(self) -> None:
        print(f"{self.reg_number} is now charged with battery of {self.battery_percentage}%")

    def get_battery_percentage(self) -> float:
        return self.battery_percentage
