from datetime import datetime
from models.pricing.pricing_strategy import PricingStrategy
from models.pricing.pricing_strategy_type import PricingStrategyType


class ConstantPricingStrategy(PricingStrategy):

    def __init__(self, price: float):
        self.price = price

    def calculate_price(self, entry_time: datetime, exit_time: datetime) -> float:
        return self.price

    @classmethod
    def get_type(cls) -> PricingStrategyType:
        return PricingStrategyType.CONSTANT
