import random

from models.pricing.pricing_strategy import PricingStrategy
from models.pricing.pricing_strategy_type import PricingStrategyType
from models.pricing.strategies.hourly_pricing_strategy import HourlyPricingStrategy
from config.server_config import ServerConfig

class PricingService:

    @staticmethod
    def calculate_pricing_charge(pricing_strategies:list[PricingStrategy]):
        for i , strategy in enumerate(pricing_strategies):
          if strategy.get_type() == PricingStrategyType.HOURLY :
            price_per_hour = ServerConfig.PRICE_PER_HOUR
            number_of_hours = random.randint(1,20)
            # You can also have factory class here 
            pricing_strategies[i] = HourlyPricingStrategy(price_per_hour,number_of_hours)

        return sum(strategy.calculate_price() for strategy in pricing_strategies)

