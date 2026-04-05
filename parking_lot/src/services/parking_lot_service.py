import threading
import uuid
from datetime import datetime
from typing import Optional, TYPE_CHECKING
from models.parking.parking_slot import ParkingSlot
from models.parking.parking_slot_status import ParkingSlotStatus
from models.vehicle.vehicle import Vehicle
from models.ticket.ticket import Ticket

if TYPE_CHECKING:
    from models.parking.parking_lot import ParkingLot
    from models.parking.strategies.find_slot_strategy import FindSlotStrategy


class ParkingLotService:

    def __init__(self, parking_lot: "ParkingLot", find_slot_strategy: "FindSlotStrategy"):
        self.parking_lot = parking_lot
        self.find_slot_strategy = find_slot_strategy
        self._lock = threading.Lock()
        self._vehicle_slot_mapping: dict[str, ParkingSlot] = {}
        self._vehicle_ticket_mapping: dict[str, Ticket] = {}

    def park_car(self, vehicle: Vehicle) -> Optional[Ticket]:
        with self._lock:
            slot = self.find_slot_strategy.find_slot(self.parking_lot, vehicle)

            if slot is None:
                print("No available slot to park the vehicle")
                return None

            slot.park_vehicle(vehicle)
            self._vehicle_slot_mapping[vehicle.reg_number] = slot

            ticket = Ticket(
                ticket_id=uuid.uuid4().int % 1000000,
                entry_time=datetime.now(),
                exit_time=None,
                vehicle=vehicle,
                parking_slot=slot,
                pricing_strategies=[],
                payment_strategy=None
            )
            self._vehicle_ticket_mapping[vehicle.reg_number] = ticket

            print(f"Vehicle parked at Floor {slot.parking_floor.floor_number}, Slot {slot.slot_number}")
            return ticket

    def unpark_car(self, vehicle: Vehicle) -> Optional[Ticket]:
        with self._lock:
            if vehicle.reg_number not in self._vehicle_slot_mapping:
                print("Vehicle not found in the parking lot")
                return None

            slot = self._vehicle_slot_mapping.pop(vehicle.reg_number)
            slot.status = ParkingSlotStatus.AVAILABLE
            slot.vehicle = None

            ticket = self._vehicle_ticket_mapping.pop(vehicle.reg_number)
            ticket.exit_time = datetime.now()

            print(f"Vehicle unparked from Floor {slot.parking_floor.floor_number}, Slot {slot.slot_number}")
            return ticket

    def get_ticket(self, vehicle: Vehicle) -> Optional[Ticket]:
        return self._vehicle_ticket_mapping.get(vehicle.reg_number)
