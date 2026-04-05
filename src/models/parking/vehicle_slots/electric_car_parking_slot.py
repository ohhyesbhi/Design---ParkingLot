
from parking.parking_slot import ParkingSlot
from parking.parking_floor import ParkingFloor
from vechile_models.enums.vehicle_type import VehicleType


class ElectricCarParkingSlot(ParkingSlot):

    def __init__(self, slot_number: int, floor: ParkingFloor):
        super().__init__([VehicleType.ELECTRIC_CAR], slot_number, floor)

    def charge_vehicle(self):
        print(f"Charging electric vehicle at slot {self.slot_number}")