from abc import ABC , abstractmethod
from enums.vehicle_type import VehicleType


# Without __repr__ : 
# car = Car("KA-01-1234", "Red")
# print(car)  # 😕 <__main__.Car object at 0x000001A2B3C4D5E6>

# With __repr__ : 
# car = Car("KA-01-1234", "Red")
# print(car)  # ✅ CAR(reg=KA-01-1234, color=Red)

class Vehicle(ABC):

    def __init__(self, reg_number : str , color : str , vehicle_type : VehicleType ):

        self.reg_number = reg_number
        self.color = color
        self.vehicle_type = vehicle_type


    #__repr__ is not functionally critical to the parking system, but it makes debugging dramatically easier
    def __repr__(self):
        return f"{self.vehicle_type.value} ( reg = {self.re_number} , color = {self.color})"
         

