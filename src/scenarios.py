"""
Parking Lot - Scenario Events
"""

from datetime import datetime, timedelta

from models.pricing.strategies.composite_pricing_strategy import CompositePricingStrategy
from models.payment.strategies.card_payment_strategy import CardPaymentStrategy
from models.payment.strategies.cash_payment_strategy import CashPaymentStrategy
from models.payment.strategies.fasttag_payment_strategy import FastTagPaymentStrategy

from parking_system import system


def park(vehicle):
    """Park a vehicle"""
    ticket = system.service.park_car(vehicle)
    if ticket:
        system.active_tickets[vehicle.reg_number] = {
            'ticket': ticket,
            'vehicle': vehicle
        }
        print(f"[PARK] {vehicle.vehicle_type.value}: {vehicle.reg_number}")
        print(f"      Floor {ticket.parking_slot.parking_floor.floor_number}, Slot {ticket.parking_slot.slot_number}")
    else:
        print(f"[FAIL] No slot for {vehicle.reg_number}")
    return ticket


def unpark(reg_number, payment="card", hours=1):
    """Unpark a vehicle"""
    if reg_number not in system.active_tickets:
        print(f"[ERROR] {reg_number} not found")
        return False

    data = system.active_tickets[reg_number]
    ticket = data['ticket']
    vehicle = data['vehicle']

    ticket.entry_time = datetime.now() - timedelta(hours=hours)
    ticket.exit_time = datetime.now()

    if len(system.pricing_strategies) == 1:
        price = system.pricing_strategies[0].calculate_price(ticket.entry_time, ticket.exit_time)
    else:
        price = CompositePricingStrategy(system.pricing_strategies).calculate_price(ticket.entry_time, ticket.exit_time)

    methods = {"card": CardPaymentStrategy(), "cash": CashPaymentStrategy(), "fasttag": FastTagPaymentStrategy()}
    methods[payment].pay(price)

    system.service.unpark_car(vehicle)
    del system.active_tickets[reg_number]

    print(f"[UNPARK] {vehicle.vehicle_type.value}: {reg_number} | {hours}h | Rs.{price:.2f} | {payment.upper()}")
    return True


def change_pricing(pricing_strategies):
    """Change pricing strategy"""
    system.pricing_strategies = pricing_strategies
    print("[PRICING] Changed")


def status():
    """Show parking status"""
    print("\n[STATUS]")
    for floor in system.parking_lot.floors:
        type_stats = {}
        for slot in floor.slots:
            key = slot.supported_vehicle_types[0].value
            if key not in type_stats:
                type_stats[key] = {"total": 0, "occupied": 0}
            type_stats[key]["total"] += 1
            if not slot.is_available():
                type_stats[key]["occupied"] += 1

        print(f"  Floor {floor.floor_number}:", end=" ")
        parts = [f"{stats['occupied']}/{stats['total']} {vtype}" for vtype, stats in type_stats.items()]
        print(", ".join(parts))
    print(f"  Parked: {len(system.active_tickets)} vehicles")
