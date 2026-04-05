from parking_slot import ParkingSlot

class ParkingFloor:

    def __init__(self,floor_number:int,parking_slots:list[ParkingSlot]):

        self.floor_number = floor_number
        self.parking_slots = parking_slots

    def add_parking_slot(self,slot:ParkingSlot):
        self.parking_slots.append(slot)
        return True


        