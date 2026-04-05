from typing import TYPE_CHECKING
from models.parking.parking_slot import ParkingSlot
from models.vehicle.vehicle_type import VehicleType

if TYPE_CHECKING:
    from models.parking.parking_floor import ParkingFloor


class BikeParkingSlot(ParkingSlot):

    def __init__(self, slot_number: int, floor: "ParkingFloor"):
        super().__init__([VehicleType.BIKE], slot_number, floor)
