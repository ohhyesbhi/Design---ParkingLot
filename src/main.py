"""
Parking Lot - Main Entry Point
"""

from models.vehicle.vehicles.car import Car
from models.vehicle.vehicles.bike import Bike
from models.vehicle.vehicles.electric_car import ElectricCar

from models.pricing.strategies.hourly_pricing_strategy import HourlyPricingStrategy
from models.pricing.strategies.constant_pricing_strategy import ConstantPricingStrategy

from parking_system import system
from scenarios import park, unpark, change_pricing, status


# ============================================================================
# RUN DEMO
# ============================================================================

def run():
    print("\n" + "="*60)
    print("  PARKING LOT SYSTEM - SCENARIOS")
    print("="*60 + "\n")

    # Create vehicles
    car1 = Car("DL-01-CA-1234", "Red")
    bike1 = Bike("DL-02-BI-5678", "Blue")
    ecar1 = ElectricCar("DL-03-EC-9012", "White", 85)
    bike2 = Bike("DL-04-BI-3456", "Black")
    car2 = Car("MH-01-CA-1111", "Yellow")
    car3 = Car("MH-02-CA-2222", "Orange")

    # SCENARIO 1: Initialize and park
    print("\n--- SCENARIO 1: Park 4 Vehicles ---")
    system.init([
        ConstantPricingStrategy(20),
        HourlyPricingStrategy(10)
    ])
    print("[PRICING] Base Rs.20 + Rs.10/hour")

    park(car1)
    park(bike1)
    park(ecar1)
    park(bike2)
    status()

    # SCENARIO 2: Unpark
    print("\n--- SCENARIO 2: Unpark 2 Vehicles ---")
    unpark("DL-01-CA-1234", payment="card", hours=2)
    unpark("DL-03-EC-9012", payment="fasttag", hours=3.5)
    status()

    # SCENARIO 3: Add floor
    print("\n--- SCENARIO 3: Add Floor & Park More ---")
    system.add_floor(3, [("CAR", 5), ("BIKE", 3)])
    park(car2)
    park(car3)
    status()

    # SCENARIO 4: Change pricing and unpark all
    print("\n--- SCENARIO 4: Change Pricing & Unpark All ---")
    change_pricing([HourlyPricingStrategy(25)])
    print("[PRICING] Rs.25/hour")

    for reg in list(system.active_tickets.keys()):
        unpark(reg, payment="cash", hours=2)
    status()

    print("\n" + "="*60)
    print("  ALL SCENARIOS COMPLETED!")
    print("="*60 + "\n")


if __name__ == "__main__":
    run()
