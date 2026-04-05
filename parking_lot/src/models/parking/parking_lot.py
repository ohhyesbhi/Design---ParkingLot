from typing import List, TYPE_CHECKING
from models.pricing.pricing_strategy import PricingStrategy

if TYPE_CHECKING:
    from models.parking.parking_floor import ParkingFloor


class ParkingLot:

    def __init__(self, floors: List["ParkingFloor"], pricing_strategies: List[PricingStrategy] = None):
        self.floors = floors
        self.pricing_strategies = pricing_strategies or []

    def add_parking_floor(self, floor: "ParkingFloor") -> None:
        self.floors.append(floor)

    def remove_parking_floor(self, floor: "ParkingFloor") -> None:
        self.floors.remove(floor)
