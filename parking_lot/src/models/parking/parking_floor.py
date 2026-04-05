from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from models.parking.parking_slot import ParkingSlot


class ParkingFloor:

    def __init__(self, floor_number: int, parking_slots: List["ParkingSlot"] = None):
        self.floor_number = floor_number
        self.parking_slots = parking_slots or []

    @property
    def slots(self) -> List["ParkingSlot"]:
        return self.parking_slots

    def add_parking_slot(self, slot: "ParkingSlot") -> bool:
        self.parking_slots.append(slot)
        return True
