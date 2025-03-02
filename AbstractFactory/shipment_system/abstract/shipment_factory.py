from abc import ABC, abstractmethod

class ShipmentFactory(ABC):
    """Abstract factory interface for creating shipments."""
    
    @abstractmethod
    def create_air_shipment(self):
        """Create an air shipment."""
        pass
    
    @abstractmethod
    def create_ground_shipment(self):
        """Create a ground shipment."""
        pass
    
    @abstractmethod
    def create_water_shipment(self):
        """Create a water shipment."""
        pass