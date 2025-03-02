from shipment_system.abstract.shipment import Shipment

class FedExAirShipment(Shipment):
    """FedEx Air Shipment implementation."""
    
    def __init__(self):
        super().__init__()
        self.first_class = False
    
    def set_first_class(self, first_class):
        """Set whether this is a first-class shipment."""
        self.first_class = first_class
    
    def calculate_cost(self):
        """Calculate the cost of the FedEx air shipment."""
        base_cost = 120.0 + (self.weight * 2.8)
        return base_cost * 1.7 if self.first_class else base_cost
    
    def track_shipment(self):
        """Track the FedEx air shipment."""
        return f"Tracking FedEx Air shipment {self.tracking_number}"
    
    def get_estimated_delivery_time(self):
        """Get the estimated delivery time for the FedEx air shipment."""
        return "Overnight" if self.first_class else "2-3 business days"
    
    def request_overnight_delivery(self):
        """Request overnight delivery for this shipment."""
        return True