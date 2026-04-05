from enum import Enum

class ParkingSlotStatus(Enum):
    AVAILABLE = "available"
    OCCUPIED = "occupied"
    RESERVED = "reserved"
    OUT_OF_SERVICE = "out_of_service"