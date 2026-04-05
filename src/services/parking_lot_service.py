



import threading
import uuid
from datetime import datetime

from models.parking.parking_lot import ParkingLot
from models.parking.parking_slot import ParkingSlot
from models.parking.parking_slot_status import ParkingSlotStatus
from models.vechile_models.vehicle import Vehicle
from models.parking.strategy.find_slot_strategy import FindSlotStrategy
from models.tickets.ticket import Ticket

class ParkingLotService:

    def __init__(self, parking_lot: ParkingLot, find_slot_strategy: FindSlotStrategy):
        self.parking_lot = parking_lot
        self.find_slot_strategy = find_slot_strategy
        self._lock = threading.Lock()
        self._vehicle_slot_mapping: dict[str, ParkingSlot] = {}
        self._vehicle_ticket_mapping: dict[str, Ticket] = {}

    def park_car(self, vehicle: Vehicle) -> Ticket:
        # with self._lock = "Lock this section for one thread at a time"
        # QUESTOION -: How we will get to know that locks are released ? 
        # ANSWER -: Normal exit - lock released
        with self._lock:
            slot = self.find_slot_strategy.findSlot(self.parking_lot, vehicle)
            
            if slot is None:
                print("No available slot to park the vehicle")
                return None
            
            slot.park_vehicle(vehicle)
            self._vehicle_slot_mapping[vehicle.reg_number] = slot
            
            ticket = Ticket(
                id=uuid.uuid4().int % 1000000,
                entry_time=datetime.now(),
                exit_time=None,
                vehicle=vehicle,
                parking_slot=slot,
                pricing_strategies=[],
                payment_strategy=None
            )
            self._vehicle_ticket_mapping[vehicle.reg_number] = ticket
            
            print(f"Vehicle parked at Floor {slot.parking_floor.floor_number}, Slot {slot.slot_number}")
            print(f"Ticket generated for Vehicle: {vehicle.reg_number}, Entry Time: {ticket.entry_time}")
            return ticket

    def unpark_car(self, vehicle: Vehicle) -> Ticket:
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

    def get_ticket(self, vehicle: Vehicle) -> Ticket:
        return self._vehicle_ticket_mapping.get(vehicle.reg_number)
    

# Notes -: Without lock, two threads can interfere with each other:
# Key rule: Only one thread can enter the block at a time. Others wait

# This:
# with self._lock:
#     # critical section

# # Is equivalent to:
# self._lock.acquire()
# try:
#     # critical section
# finally:
#     self._lock.release()