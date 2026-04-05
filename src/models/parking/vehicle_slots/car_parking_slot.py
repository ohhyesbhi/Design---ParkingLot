
from parking.parking_slot import ParkingSlot
from parking.parking_floor import ParkingFloor
from vechile_models.enums.vehicle_type import VehicleType

class CarParkingSlot(ParkingSlot):

    def __init__(self, slot_number: int, floor: ParkingFloor):
          super().__init__([VehicleType.CAR], slot_number, floor)
    