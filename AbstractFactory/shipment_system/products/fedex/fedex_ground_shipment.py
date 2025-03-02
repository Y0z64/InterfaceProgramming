from shipment_system.abstract.shipment import Shipment

class FedExGroundShipment(Shipment):
    """FedEx Ground Shipment implementation."""
    
    def __init__(self):
        super().__init__()
        self.local_delivery = False
    
    def set_local_delivery(self, local_delivery):
        """Set whether this is a local delivery."""
        self.local_delivery = local_delivery
    
    def calculate_cost(self):
        """Calculate the cost of the FedEx ground shipment."""
        base_cost = 45.0 + (self.weight * 1.1)
        return base_cost * 0.9 if self.local_delivery else base_cost
    
    def track_shipment(self):
        """Track the FedEx ground shipment."""
        return f"Tracking FedEx Ground shipment {self.tracking_number}"
    
    def get_estimated_delivery_time(self):
        """Get the estimated delivery time for the FedEx ground shipment."""
        return "1-2 business days" if self.local_delivery else "3-5 business days"
    
    def request_residential_delivery(self):
        """Request residential delivery for this shipment."""
        return True