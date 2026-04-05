from datetime import datetime
from pricing.pricing_strategy import PricingStrategy
from pricing.pricing_strategy_type import PricingStrategyType


class ConstantPricingStrategy(PricingStrategy):

    def __init__(self, price: float):
        self.price = price

    def calculate_price(self) -> float:
        return self.price
    
    @classmethod
    def get_type(cls) -> PricingStrategyType:
        return PricingStrategyType.CONSTANT

        