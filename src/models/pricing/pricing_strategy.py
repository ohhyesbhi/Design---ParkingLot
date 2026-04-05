
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List


class PricingStrategy(ABC):

    @abstractmethod
    def calculate_price(self, entry_time: datetime, exit_time: datetime) -> float:
        pass

    @classmethod
    #@staticmethod
    @abstractmethod
    def get_type(cls) -> str:
        pass


# Note -: 

# @abstractmethod
# @staticmethod
# def get_type() -> str:
#     pass

# This doesn't enforce implementation. Python's abstract method check only looks at the first decorator,
# so @staticmethod bypasses the enforcement. Subclasses can completely omit get_type() and Python won't complain.

# My next question -: So should i conclude that in abstract classes we cant have static method because it is not enforced ?
# ANS  -: Not exactly. You can have static methods in abstract classes, but don't make them abstract.

# from abc import ABC, abstractmethod

# class Shape(ABC):
    
#     # ✅ Static method - shared utility, not abstract
#     @staticmethod
#     def validate_color(color: str) -> bool:
#         return color in ["red", "blue", "green"]
    
#     # ✅ Class method - abstract + returns type
#     @classmethod
#     @abstractmethod
#     def get_shape_type(cls) -> str:
#         pass
    
#     # ✅ Instance method - abstract behavior
#     @abstractmethod
#     def calculate_area(self) -> float