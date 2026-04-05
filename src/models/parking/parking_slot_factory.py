from typing import List, TYPE_CHECKING
from models.vehicle.vehicle_type import VehicleType

if TYPE_CHECKING:
    from models.parking.parking_slot import ParkingSlot
    from models.parking.parking_floor import ParkingFloor


class ParkingSlotFactory:

    @staticmethod
    def create_slot(
        slot_type: VehicleType,
        slot_number: int,
        floor: "ParkingFloor"
    ) -> "ParkingSlot":
        from models.parking.parking_slots.car_parking_slot import CarParkingSlot
        from models.parking.parking_slots.bike_parking_slot import BikeParkingSlot
        from models.parking.parking_slots.electric_car_parking_slot import ElectricCarParkingSlot
        from models.parking.parking_slots.electric_bike_parking_slot import ElectricBikeParkingSlot

        slot_map = {
            VehicleType.CAR: CarParkingSlot,
            VehicleType.BIKE: BikeParkingSlot,
            VehicleType.ELECTRIC_CAR: ElectricCarParkingSlot,
            VehicleType.ELECTRIC_BIKE: ElectricBikeParkingSlot,
        }

        slot_class = slot_map.get(slot_type)
        if not slot_class:
            raise ValueError(f"Unknown slot type: {slot_type}")

        return slot_class(slot_number, floor)

    @staticmethod
    def create_slots_for_vehicle_type(
        vehicle_type: VehicleType,
        count: int,
        floor: "ParkingFloor",
        start_slot_number: int = 1
    ) -> List["ParkingSlot"]:
        return [
            ParkingSlotFactory.create_slot(vehicle_type, start_slot_number + i, floor)
            for i in range(count)
        ]
