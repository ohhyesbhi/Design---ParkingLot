from abc import ABC, abstractmethod
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from models.parking.parking_lot import ParkingLot
    from models.parking.parking_slot import ParkingSlot
    from models.vehicle.vehicle import Vehicle


class FindSlotStrategy(ABC):

    @abstractmethod
    def find_slot(self, parking_lot: "ParkingLot", vehicle: "Vehicle") -> Optional["ParkingSlot"]:
        pass
