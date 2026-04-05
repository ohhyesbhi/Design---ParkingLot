from typing import Optional

from vechile_models.enums.vehicle_type import VehicleType
from parking.parking_slot_status import ParkingSlotStatus
from parking.parking_floor import ParkingFloor
from vechile_models.vehicle import Vehicle


class ParkingSlot :

    # Why default values are added in last ( like vehicle and status  ) because they are throwing errors if we add them somewhere in the middle 

    def __init__(self
                 ,supported_vehicle_type : list[VehicleType] 
                 ,slot_number : int  
                 ,floor : ParkingFloor
                 ,vehicle : Optional[Vehicle] = None 
                 ,status : ParkingSlotStatus = ParkingSlotStatus.AVAILABLE
                 ):
        
        self.supported_vehicle_type = supported_vehicle_type
        self.status = status
        self.slot_number = slot_number
        self.parking_floor= floor
        self.vehicle = vehicle

    
    def park_vehicle(self,vehicle:Vehicle):

        if vehicle.vehicle_type in self.supported_vehicle_type:
            self.vehicle = vehicle
            self.status = ParkingSlotStatus.OCCUPIED
        else:
            print(f"{vehicle.vehicle_type}Vehicle type is not supported for this parking slot")

    def is_parking_supported(self,vehicle:Vehicle)->bool:
        return vehicle.vehicle_type in self.supported_vehicle_type
    
    def is_available(self)->bool:
        return self.status == ParkingSlotStatus.AVAILABLE
        






  