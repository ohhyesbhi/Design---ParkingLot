
from models.vechile_models.vehicle import Vehicle
from enums.vehicle_type import VehicleType

class Car(Vehicle):

    def __init__(self, reg_number: str, color: str):
        super().__init__(reg_number, color, VehicleType.CAR)
