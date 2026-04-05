from typing import Optional, TYPE_CHECKING
from models.vehicle.vehicle_type import VehicleType
from models.parking.parking_slot_status import ParkingSlotStatus

if TYPE_CHECKING:
    from models.parking.parking_floor import ParkingFloor
    from models.vehicle.vehicle import Vehicle


class ParkingSlot:

    def __init__(
        self,
        supported_vehicle_types: list[VehicleType],
        slot_number: int,
        floor: "ParkingFloor",
        vehicle: Optional["Vehicle"] = None,
        status: ParkingSlotStatus = ParkingSlotStatus.AVAILABLE
    ):
        self.supported_vehicle_types = supported_vehicle_types
        self.status = status
        self.slot_number = slot_number
        self.parking_floor = floor
        self.vehicle = vehicle

    def park_vehicle(self, vehicle: "Vehicle") -> bool:
        if vehicle.vehicle_type in self.supported_vehicle_types:
            self.vehicle = vehicle
            self.status = ParkingSlotStatus.OCCUPIED
            return True
        print(f"{vehicle.vehicle_type} is not supported for this parking slot")
        return False

    def is_parking_supported(self, vehicle: "Vehicle") -> bool:
        return vehicle.vehicle_type in self.supported_vehicle_types

    def is_available(self) -> bool:
        return self.status == ParkingSlotStatus.AVAILABLE
