
from abc import ABC,abstractmethod


class ElectricSlot(ABC):
    
    @abstractmethod
    def charge_vehicle(self):
        pass;