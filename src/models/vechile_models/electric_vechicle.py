from abc import ABC,abstractmethod



class ElectricChargeSupportedVehicle(ABC):

    @abstractmethod
    def charge(self)->None: 
      pass

    @abstractmethod
    def get_battery_percentage(self)->float:
      pass