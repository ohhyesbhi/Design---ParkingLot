from typing import Optional, TYPE_CHECKING
from models.parking.strategies.find_slot_strategy import FindSlotStrategy

if TYPE_CHECKING:
    from models.parking.parking_lot import ParkingLot
    from models.parking.parking_slot import ParkingSlot
    from models.vehicle.vehicle import Vehicle


class LinearSearchFindingStrategy(FindSlotStrategy):

    def find_slot(self, parking_lot: "ParkingLot", vehicle: "Vehicle") -> Optional["ParkingSlot"]:
        for floor in parking_lot.floors:
            for slot in floor.slots:
                if slot.is_available() and slot.is_parking_supported(vehicle):
                    return slot
        return None
