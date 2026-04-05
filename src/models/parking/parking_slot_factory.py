from parking.parking_slot import ParkingSlot
from parking.parking_floor import ParkingFloor
from parking.vehicle_slots.car_parking_slot import CarParkingSlot
from parking.vehicle_slots.bike_parking_slot import BikeParkingSlot
from parking.vehicle_slots.electric_car_parking_slot import ElectricCarParkingSlot
from parking.vehicle_slots.electric_bike_parking_slot import ElectricBikeParkingSlot
from vechile_models.enums.vehicle_type import VehicleType


class ParkingSlotFactory:

    @staticmethod
    def create_slot(slot_type: VehicleType, slot_number: int, floor: ParkingFloor) -> ParkingSlot:
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
        floor: ParkingFloor,
        start_slot_number: int = 1
    ) -> list[ParkingSlot]:
        return [
            ParkingSlotFactory.create_slot(vehicle_type, start_slot_number + i, floor)
            for i in range(count)
        ]
