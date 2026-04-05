"""
Parking Lot Management System
Predefined scenarios using direct vehicle classes (like cricket events)
"""
from models.parking.parking_lot import ParkingLot
from models.parking.parking_floor import ParkingFloor
from models.parking.parking_slot_factory import ParkingSlotFactory
from models.parking.strategies.linear_search_finding_strategy import LinearSearchFindingStrategy
from services.parking_lot_service import ParkingLotService


# ============================================================================
# PARKING SYSTEM
# ============================================================================

class ParkingSystem:
    def __init__(self):
        self.parking_lot = None
        self.service = None
        self.pricing_strategies = []
        self.active_tickets = {}

    def init(self, pricing_strategies):
        self.parking_lot = ParkingLot([])
        self.pricing_strategies = pricing_strategies
        self.active_tickets = {}

        floor1 = ParkingFloor(1)
        floor2 = ParkingFloor(2)

        for i in range(1, 4):
            floor1.add_parking_slot(ParkingSlotFactory.create_slot("CAR", i, floor1))
        for i in range(4, 6):
            floor1.add_parking_slot(ParkingSlotFactory.create_slot("BIKE", i, floor1))
        for i in range(1, 3):
            floor2.add_parking_slot(ParkingSlotFactory.create_slot("ELECTRIC_CAR", i, floor2))
        for i in range(3, 5):
            floor2.add_parking_slot(ParkingSlotFactory.create_slot("ELECTRIC_BIKE", i, floor2))

        self.parking_lot.add_parking_floor(floor1)
        self.parking_lot.add_parking_floor(floor2)

        self.service = ParkingLotService(self.parking_lot, LinearSearchFindingStrategy())

        print("[INIT] Parking Lot: Floor 1 (3 Car + 2 Bike), Floor 2 (2 E-Car + 2 E-Bike)")

    def add_floor(self, floor_num, slots):
        """Add a new floor with specified slots"""
        floor = ParkingFloor(floor_num)
        slot_num = 1
        for vtype, count in slots:
            for _ in range(count):
                floor.add_parking_slot(ParkingSlotFactory.create_slot(vtype, slot_num, floor))
                slot_num += 1
        self.parking_lot.add_parking_floor(floor)
        print(f"[FLOOR] Added Floor {floor_num} with {slot_num - 1} slots")


# Global instance
system = ParkingSystem()
