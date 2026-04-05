
from abc import ABC , abstractmethod

# This way Python enforces that:
# 1) Every subclass must implement get_type() (because of @abstractmethod)
# 2) It should be implemented without self (because of @staticmethod)

class PricingStrategy(ABC):

    @abstractmethod
    def calculate_price(self) -> int:
        pass

    @abstractmethod
    @staticmethod
    def get_type() -> str:
        pass