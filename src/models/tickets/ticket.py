from datetime import datetime
from typing import Optional
from vechile_models.vehicle import Vehicle
from parking.parking_slot import ParkingSlot
from pricing.pricing_strategy import PricingStrategy
from payments.payment_strategy import PaymentStrategy
from services.pricing_service import PricingService


class Ticket:

    def __init__(self
                 ,id : int
                 ,entry_time:datetime 
                 ,exit_time:Optional[datetime] 
                 ,vehicle:Vehicle 
                 ,parking_slot : ParkingSlot
                 ,pricing_strategies : list[PricingStrategy] 
                 ,payment_strategy : PaymentStrategy
                 ):
        self.id = id
        self.entry_time = entry_time
        self.exit_time = exit_time
        self.vehicle = vehicle
        self.parking_slot = parking_slot
        self.pricing_strategies = pricing_strategies
        self.payment_strategy = payment_strategy



    def calculate_and_pay(self):
       
       price = PricingService.calculate_pricing_charge(self.pricing_strategies)
       print(f"Price calculated: {price}")
       self.payment_strategy.pay(price)