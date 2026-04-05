from datetime import datetime
from typing import List
from models.pricing.pricing_strategy import PricingStrategy
from models.pricing.strategies.composite_pricing_strategy import CompositePricingStrategy


class PricingService:

    @staticmethod
    def calculate_pricing_charge(
        pricing_strategies: List[PricingStrategy],
        entry_time: datetime,
        exit_time: datetime
    ) -> float:
        if not pricing_strategies:
            return 0.0

        if len(pricing_strategies) == 1:
            return pricing_strategies[0].calculate_price(entry_time, exit_time)

        composite = CompositePricingStrategy(pricing_strategies)
        return composite.calculate_price(entry_time, exit_time)
