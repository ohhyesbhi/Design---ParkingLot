
from typing import Optional

from strategy.find_slot_strategy import FindSlotStrategy
from parking.parking_lot import ParkingLot
from parking.parking_slot import ParkingSlot
from vechile_models.vehicle import Vehicle


class LinearSearchFindingStrategy(FindSlotStrategy):
    
    def findSlot(self,parking_lot : ParkingLot,vehicle:Vehicle)->Optional[ParkingSlot]:
        floors = parking_lot.floors
        
        for floor in floors:
            for slot in floor.slots:
                if slot.is_available() and slot.is_parking_supported(vehicle):
                    print(f"Slot found: Floor {floor.floor_number}, Slot {slot.slot_number}")
                    return slot

        print("No slot available for this vehicle")
        return None