
from parking.parking_floor import ParkingFloor
from models.pricing.pricing_strategy import PricingStrategy

class ParkingLot:

    def __init__(self,floors:list[ParkingFloor],pricing_strategies:list[PricingStrategy]):
        self.floors = floors
        self.pricing_strategies = pricing_strategies
    
    def add_parking_floor(self,floor:ParkingFloor):
        self.floors.append(floor)

    def remove_parking_floor(self,floor:ParkingFloor):
        self.floors.remove(floor)
