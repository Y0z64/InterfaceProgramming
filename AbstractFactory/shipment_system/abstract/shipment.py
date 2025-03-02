from abc import ABC, abstractmethod
import random

class Shipment(ABC):
    """Abstract base class for all shipment types."""
    
    def __init__(self):
        self.tracking_number = self._generate_tracking_number()
        self.weight = 0.0
        self.destination = ""
    
    def _generate_tracking_number(self):
        """Generate a random tracking number."""
        return f"TRK-{random.randint(100000, 999999)}"
    
    def get_tracking_number(self):
        """Get the shipment tracking number."""
        return self.tracking_number
    
    def set_weight(self, weight):
        """Set the shipment weight."""
        self.weight = weight
    
    def get_weight(self):
        """Get the shipment weight."""
        return self.weight
    
    def set_destination(self, destination):
        """Set the shipment destination."""
        self.destination = destination
    
    def get_destination(self):
        """Get the shipment destination."""
        return self.destination
    
    @abstractmethod
    def calculate_cost(self):
        """Calculate the cost of the shipment."""
        pass
    
    @abstractmethod
    def track_shipment(self):
        """Track the current status of the shipment."""
        pass
    
    @abstractmethod
    def get_estimated_delivery_time(self):
        """Get the estimated delivery time for the shipment."""
        pass