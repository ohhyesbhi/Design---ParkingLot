from datetime import datetime
from pricing.pricing_strategy import PricingStrategy
from pricing.pricing_strategy_type import PricingStrategyType


class HourlyPricingStrategy(PricingStrategy):

    def __init__(self, price_per_hour: float):
        self.price_per_hour = price_per_hour

    def calculate_price(self, entry_time: datetime, exit_time: datetime) -> float:
        duration = exit_time - entry_time
        hours = duration.total_seconds() / 3600
        return self.price_per_hour * max(1, hours)

    @classmethod
    def get_type(cls) -> PricingStrategyType:
        return PricingStrategyType.HOURLY
