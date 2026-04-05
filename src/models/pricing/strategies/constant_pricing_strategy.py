from pricing.pricing_strategy import PricingStrategy
from pricing.pricing_strategy_type import PricingStrategyType

class ConstantPricingStrategy(PricingStrategy):

    def __init__( self, price:int ):
        self.price = price ;

    def calculate_price(self):
        return self.price ;
    
    @staticmethod
    def get_type()->PricingStrategyType:
        return PricingStrategyType.CONSTANT;

        