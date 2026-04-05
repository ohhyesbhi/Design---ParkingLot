
from slots.bike_slot import BikeSlot
from slots.electric_slot import ElectricSlot
from parking.parking_slot import ParkingSlot
from parking.parking_floor import ParkingFloor
from vechile_models.enums.vehicle_type import VehicleType

class ElectricCarParkingSlot(ParkingSlot,ElectricSlot,BikeSlot):


    def __init__(self,slot_number:int,floor:ParkingFloor):
        super().__init__([VehicleType.ELECTRIC_CAR],slot_number,floor)

    def charge_vehicle(self):
        print(f"charging electric vehicle")