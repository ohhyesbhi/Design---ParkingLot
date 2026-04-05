
from slots.bike_slot import BikeSlot
from slots.electric_slot import ElectricSlot
from parking.parking_slot import ParkingSlot
from parking.parking_floor import ParkingFloor
from vechile_models.enums.vehicle_type import VehicleType

class ElectricBikeParkingSlot(ParkingSlot,ElectricSlot,BikeSlot):

    def __init__(self,slot_number:int,floor:ParkingFloor):
        super().__init__([VehicleType.ELECTRIC_BIKE],slot_number,floor)

    def charge_vehicle(self):
        print(f"charging electric bike")