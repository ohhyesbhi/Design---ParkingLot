from typing import Union
from models.parking.parking_slot import ParkingSlot
from models.parking.parking_floor import ParkingFloor


class ParkingSlotFactory:

    @staticmethod
    def create_slot(
        slot_type: Union[str, "VehicleType"],
        slot_number: int,
        floor: ParkingFloor
    ) -> ParkingSlot:
        from models.parking.parking_slots.car_parking_slot import CarParkingSlot
        from models.parking.parking_slots.bike_parking_slot import BikeParkingSlot
        from models.parking.parking_slots.electric_car_parking_slot import ElectricCarParkingSlot
        from models.parking.parking_slots.electric_bike_parking_slot import ElectricBikeParkingSlot

        slot_map = {
            "CAR": CarParkingSlot,
            "BIKE": BikeParkingSlot,
            "ELECTRIC_CAR": ElectricCarParkingSlot,
            "ELECTRIC_BIKE": ElectricBikeParkingSlot,
        }

        slot_class = slot_map.get(slot_type)
        if not slot_class:
            raise ValueError(f"Unknown slot type: {slot_type}")

        return slot_class(slot_number, floor)

