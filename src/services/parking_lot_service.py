



import datetime
import random

from models.parking.parking_lot import ParkingLot
from models.parking.parking_slot import ParkingSlot
from models.parking.parking_slot_status import ParkingSlotStatus
from models.vechile_models.vehicle import Vehicle
from models.parking.strategy.find_slot_strategy import FindSlotStrategy
from models.tickets.ticket import Ticket

class ParkingLotService:

    def __init__(self,parking_lot:ParkingLot,find_slot_strategy:FindSlotStrategy):
        self.parking_lot = parking_lot
        self.find_slot_strategy = find_slot_strategy
        self.vechicle_slot_mapping : dict[Vehicle, ParkingSlot] = {} # to keep track of which vehicle is parked in which slot
        self.vechicle_ticket_mapping : dict[Vehicle, Ticket] = {} # to keep track of which vehicle is associated with which ticket

    
    def park_car(self,vehicle:Vehicle):
       slot = self.find_slot_strategy.findSlot(self.parking_lot,vehicle)

       if slot is not None:
            slot.park_vehicle(vehicle)
            self.vechicle_slot_mapping[vehicle] = slot
            print(f"Vehicle parked at Floor {slot.floor_number}, Slot {slot.slot_number}")

            # Create a ticket for the parked vehicle
            ticket = Ticket(id=random.randint(1, 1000),entry_time=datetime.now(), exit_time=None, vehicle=vehicle, parking_slot=slot, pricing_strategies=slot.pricing_strategies, payment_strategy=None)
            self.vechicle_ticket_mapping[vehicle] = ticket.id
            print(f"Ticket generated for Vehicle: {vehicle.license_plate}, Entry Time: {ticket.entry_time}")
       else:
            print("No available slot to park the vehicle")

    def unpark_car(self,vehicle:Vehicle):
        if vehicle in self.vechicle_slot_mapping:
            slot = self.vechicle_slot_mapping[vehicle]
            slot.status = ParkingSlotStatus.AVAILABLE
            slot.vehicle = None
            del self.vechicle_slot_mapping[vehicle]
            del self.vechicle_ticket_mapping[vehicle]
            print(f"Vehicle unparked from Floor {slot.floor_number}, Slot {slot.slot_number}")
        else:
            print("Vehicle not found in the parking lot")