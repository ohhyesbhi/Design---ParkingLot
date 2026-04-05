from pricing.pricing_strategy import PricingStrategy
from pricing.pricing_strategy_type import PricingStrategyType


class HourlyPricingStrategy(PricingStrategy):

    def __init__( self, price_per_hour:int , number_of_hours):
        self.price_per_hour = price_per_hour 
        self.number_of_hours = number_of_hours 


    def calculate_price(self)->int:
        return self.price_per_hour * self.number_of_hours

    @staticmethod
    def get_type()->PricingStrategyType:
        return PricingStrategyType.HOURLY
