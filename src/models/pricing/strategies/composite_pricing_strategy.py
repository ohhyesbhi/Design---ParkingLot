from datetime import datetime
from typing import List
from models.pricing.pricing_strategy import PricingStrategy
from models.pricing.pricing_strategy_type import PricingStrategyType


class CompositePricingStrategy(PricingStrategy):

    def __init__(self, strategies: List[PricingStrategy]):
        self.strategies = strategies

    def calculate_price(self, entry_time: datetime, exit_time: datetime) -> float:
        return sum(
            strategy.calculate_price(entry_time, exit_time)
            for strategy in self.strategies
        )

    def add_strategy(self, strategy: PricingStrategy):
        self.strategies.append(strategy)

    @classmethod
    def get_type(cls) -> PricingStrategyType:
        return PricingStrategyType.CONSTANT
