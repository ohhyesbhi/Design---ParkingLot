from datetime import datetime
from typing import List
from pricing.pricing_strategy import PricingStrategy
from pricing.pricing_strategy_type import PricingStrategyType


# Composite Pattern = Treat "one thing" and "many things" identically

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


# Note -: # Both work the same way

# single.calculate_price()     # 100
# group.calculate_price()      # 100 (sum of all inside)

# Rule of Thumb : 
# If your code does for item in items: result += item.calculate() — you need composite.
