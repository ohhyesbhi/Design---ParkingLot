from typing import TYPE_CHECKING
from models.parking.parking_slot import ParkingSlot
from models.vehicle.vehicle_type import VehicleType

if TYPE_CHECKING:
    from models.parking.parking_floor import ParkingFloor


class ElectricBikeParkingSlot(ParkingSlot):

    def __init__(self, slot_number: int, floor: "ParkingFloor"):
        super().__init__([VehicleType.ELECTRIC_BIKE], slot_number, floor)

    def charge_vehicle(self) -> None:
        print(f"Charging electric bike at slot {self.slot_number}")
