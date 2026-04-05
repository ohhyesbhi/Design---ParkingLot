
from abc import ABC , abstractmethod
from typing import Optional
from parking.parking_lot import ParkingLot
from parking.parking_slot import ParkingSlot
from vechile_models.vehicle import Vehicle


class FindSlotStrategy(ABC) : 

    @abstractmethod
    def findSlot(self, parking_lot: ParkingLot, vehicle: Vehicle) -> Optional[ParkingSlot]:
        pass
    
