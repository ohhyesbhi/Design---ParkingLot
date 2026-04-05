# Parking Lot System

A well-structured parking lot management system demonstrating object-oriented design patterns in Python.

## Project Structure

```
parking_lot/
└── src/
    ├── main.py                       # Interactive CLI application
    ├── config/
    │   └── server_config.py          # Configuration settings
    ├── models/
    │   ├── parking/
    │   │   ├── parking_lot.py        # Main parking lot entity
    │   │   ├── parking_floor.py      # Individual floor
    │   │   ├── parking_slot.py       # Base parking slot
    │   │   ├── parking_slot_status.py # Slot status enum
    │   │   ├── parking_slot_factory.py # Factory for slot creation
    │   │   ├── strategies/
    │   │   │   ├── find_slot_strategy.py       # Abstract strategy
    │   │   │   └── linear_search_finding_strategy.py
    │   │   └── parking_slots/
    │   │       ├── car_parking_slot.py
    │   │       ├── bike_parking_slot.py
    │   │       ├── electric_car_parking_slot.py
    │   │       └── electric_bike_parking_slot.py
    │   ├── vehicle/
    │   │   ├── vehicle.py            # Base vehicle
    │   │   ├── vehicle_type.py       # Vehicle type enum
    │   │   ├── electric_vehicle.py    # Electric vehicle interface
    │   │   └── vehicles/
    │   │       ├── car.py
    │   │       ├── bike.py
    │   │       ├── electric_car.py
    │   │       └── electric_bike.py
    │   ├── pricing/
    │   │   ├── pricing_strategy.py    # Abstract pricing
    │   │   ├── pricing_strategy_type.py
    │   │   └── strategies/
    │   │       ├── hourly_pricing_strategy.py
    │   │       ├── constant_pricing_strategy.py
    │   │       └── composite_pricing_strategy.py
    │   ├── payment/
    │   │   ├── payment_strategy.py   # Abstract payment
    │   │   └── strategies/
    │   │       ├── card_payment_strategy.py
    │   │       ├── cash_payment_strategy.py
    │   │       └── fasttag_payment_strategy.py
    │   └── ticket/
    │       └── ticket.py             # Parking ticket
    └── services/
        ├── parking_lot_service.py     # Business logic
        └── pricing_service.py        # Pricing calculation
```

## Features

### 1. Vehicle Types
- **Car** - Standard car
- **Bike** - Two-wheeler
- **Electric Car** - Electric vehicle with battery
- **Electric Bike** - Electric two-wheeler

### 2. Parking Slot Types
| Slot Type | Vehicles Accepted |
|-----------|------------------|
| `CarParkingSlot` | Car |
| `BikeParkingSlot` | Bike |
| `ElectricCarParkingSlot` | Electric Car |
| `ElectricBikeParkingSlot` | Electric Bike |

### 3. Parking Slot Status
```python
AVAILABLE       # Slot is free
OCCUPIED        # Slot has a vehicle
RESERVED        # Slot is reserved
OUT_OF_SERVICE  # Slot is not available
```

## Design Patterns Used

### 1. Strategy Pattern
Used for slot finding and pricing strategies.

**Slot Finding Strategy**
```python
# Abstract base
class FindSlotStrategy(ABC):
    @abstractmethod
    def find_slot(self, parking_lot, vehicle) -> ParkingSlot:
        pass

# Concrete implementation
class LinearSearchFindingStrategy(FindSlotStrategy):
    def find_slot(self, parking_lot, vehicle):
        # Search floors and slots linearly
        for floor in parking_lot.floors:
            for slot in floor.slots:
                if slot.is_available() and slot.is_parking_supported(vehicle):
                    return slot
        return None
```

**Pricing Strategy**
```python
class PricingStrategy(ABC):
    @abstractmethod
    def calculate_price(self, entry_time, exit_time) -> float:
        pass
    
    @classmethod
    @abstractmethod
    def get_type(cls) -> str:
        pass
```

### 2. Factory Pattern
Creates parking slots based on vehicle type.

```python
class ParkingSlotFactory:
    @staticmethod
    def create_slot(slot_type: VehicleType, slot_number: int, floor: ParkingFloor):
        slot_map = {
            VehicleType.CAR: CarParkingSlot,
            VehicleType.BIKE: BikeParkingSlot,
            VehicleType.ELECTRIC_CAR: ElectricCarParkingSlot,
            VehicleType.ELECTRIC_BIKE: ElectricBikeParkingSlot,
        }
        return slot_map[slot_type](slot_number, floor)
    
    @staticmethod
    def create_slots_for_vehicle_type(vehicle_type, count, floor, start=1):
        return [create_slot(vehicle_type, start+i, floor) for i in range(count)]
```

### 3. Composite Pattern
Combines multiple pricing strategies.

```python
class CompositePricingStrategy(PricingStrategy):
    def __init__(self, strategies: List[PricingStrategy]):
        self.strategies = strategies
    
    def calculate_price(self, entry_time, exit_time) -> float:
        return sum(s.calculate_price(entry_time, exit_time) for s in self.strategies)
```

**Usage:**
```python
composite = CompositePricingStrategy([
    ConstantPricingStrategy(20),    # Base rate
    HourlyPricingStrategy(10),     # Per hour
])

price = composite.calculate_price(entry_time, exit_time)  # Total: 30 + (10 * hours)
```

### 4. Thread Safety
Uses `threading.Lock` for concurrent access.

```python
class ParkingLotService:
    def __init__(self, parking_lot, find_slot_strategy):
        self._lock = threading.Lock()
        self._vehicle_slot_mapping = {}
    
    def park_car(self, vehicle):
        with self._lock:  # Only one thread can enter at a time
            # Critical section
```

## Usage Example

```python
from models.parking.parking_lot import ParkingLot
from models.parking.parking_floor import ParkingFloor
from models.parking.parking_slot_factory import ParkingSlotFactory
from models.parking.strategies.linear_search_finding_strategy import LinearSearchFindingStrategy
from models.vehicle.vehicles.car import Car
from models.vehicle.vehicle_type import VehicleType
from services.parking_lot_service import ParkingLotService

# Create parking lot with floors and slots
floor1 = ParkingFloor(1)
slots = ParkingSlotFactory.create_slots_for_vehicle_type(
    VehicleType.CAR, 
    count=5, 
    floor=floor1
)
for slot in slots:
    floor1.add_parking_slot(slot)

parking_lot = ParkingLot([floor1])
strategy = LinearSearchFindingStrategy()
service = ParkingLotService(parking_lot, strategy)

# Park a car
car = Car("KA-01-1234", "Red")
ticket = service.park_car(car)

# Unpark the car
ticket = service.unpark_car(car)
```

## Pricing Strategies

### Constant Pricing
Flat rate regardless of duration.

```python
strategy = ConstantPricingStrategy(50)  # Fixed ₹50
```

### Hourly Pricing
Based on time spent.

```python
strategy = HourlyPricingStrategy(20)  # ₹20 per hour
```

### Composite Pricing
Combines multiple strategies.

```python
strategy = CompositePricingStrategy([
    ConstantPricingStrategy(20),    # Base ₹20
    HourlyPricingStrategy(10),     # + ₹10/hour
])
```

## Payment Methods

```python
from models.payment.strategies.card_payment_strategy import CardPaymentStrategy
from models.payment.strategies.cash_payment_strategy import CashPaymentStrategy
from models.payment.strategies.fasttag_payment_strategy import FastTagPaymentStrategy

payment = CardPaymentStrategy()
payment.pay(150)  # Payment done using card: 150
```

## Key Concepts

### Abstract Base Classes
Used for `Vehicle`, `ParkingSlot`, `PricingStrategy`, `PaymentStrategy`, `FindSlotStrategy`.

### Enums
- `VehicleType` - Types of vehicles
- `ParkingSlotStatus` - Slot availability states
- `PricingStrategyType` - Types of pricing

### Type Hints
All methods use Python type hints for better code documentation.

### `TYPE_CHECKING`
Used to avoid circular imports:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.parking.parking_floor import ParkingFloor

class ParkingSlot:
    def __init__(self, floor: "ParkingFloor"):  # String quote for type hint
        self.floor = floor
```

### `@property` Decorator
Provides clean API access:
```python
class ParkingFloor:
    @property
    def slots(self):
        return self.parking_slots

# Usage: floor.slots instead of floor.parking_slots
```

### `@classmethod` with `@abstractmethod`
Enforces subclass implementation while accessing class:
```python
class PricingStrategy(ABC):
    @classmethod
    @abstractmethod
    def get_type(cls) -> str:
        pass
```

## Running the System

### Predefined Scenarios (Event-Driven)

The system uses predefined scenarios (like cricket events) instead of interactive input:

```bash
cd src
python main.py
```

**Run Modes:**
| Option | Description |
|--------|-------------|
| 1 | Run All Scenarios (Full Demo) - 24 predefined events |
| 2 | Run Custom Scenarios |

**Scenario Events:**
```python
# Define events (scenarios) like cricket events
ParkCar("DL-01-CA-1234", "Red")
ParkBike("DL-02-BI-5678", "Blue")
ParkElectricCar("DL-03-EC-9012", "White", 85)
ShowStatus()
UnparkVehicle("DL-01-CA-1234", "card", stay_hours=2)
ChangePricing([HourlyPricingStrategy(25)])
```

**Sample Output:**
```
============================================================
  SCENARIO: Park Car: DL-01-CA-1234
============================================================

[VEHICLE] Created: Car
  Reg: DL-01-CA-1234, Color: Red

[SUCCESS] Vehicle Parked!
  Ticket ID: 526597
  Floor: 1, Slot: 1

============================================================
  SCENARIO: Unpark Vehicle: DL-01-CA-1234
============================================================

[DURATION] Stayed for: 2.00 hours

[PRICE CALCULATION]
  Base Rate: Rs.20
  Hourly (2.00h x Rs.10): Rs.20.00

  TOTAL: Rs.40.00

[PAYMENT] Processing via CARD...
Payment done using card: 40.00

[SUCCESS] Vehicle DL-01-CA-1234 unparked!
```

## All Classes Used

The interactive app uses ALL classes defined in the project:

| Category | Classes |
|----------|---------|
| **Vehicle** | Vehicle (ABC), Car, Bike, ElectricCar, ElectricBike |
| **Parking** | ParkingLot, ParkingFloor, ParkingSlot, ParkingSlotFactory |
| **Slot Types** | CarParkingSlot, BikeParkingSlot, ElectricCarParkingSlot, ElectricBikeParkingSlot |
| **Strategy** | FindSlotStrategy, LinearSearchFindingStrategy |
| **Pricing** | PricingStrategy, ConstantPricingStrategy, HourlyPricingStrategy, CompositePricingStrategy |
| **Payment** | PaymentStrategy, CardPaymentStrategy, CashPaymentStrategy, FastTagPaymentStrategy |
| **Service** | ParkingLotService, PricingService |
| **Ticket** | Ticket |

## Future Enhancements

- [ ] Add more slot finding strategies (nearest, by floor preference)
- [ ] Support for multiple parking lots
- [ ] Database persistence
- [ ] Payment integration
- [ ] Admin dashboard
- [ ] Real-time slot availability tracking
