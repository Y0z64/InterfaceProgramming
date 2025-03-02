from shipment_system.abstract.shipment import Shipment

class DHLAirShipment(Shipment):
    """DHL Air Shipment implementation."""
    
    def __init__(self):
        super().__init__()
        self.express_air = False
    
    def set_express_air(self, express_air):
        """Set whether this is an express air shipment."""
        self.express_air = express_air
    
    def calculate_cost(self):
        """Calculate the cost of the DHL air shipment."""
        base_cost = 100.0 + (self.weight * 2.5)
        return base_cost * 1.5 if self.express_air else base_cost
    
    def track_shipment(self):
        """Track the DHL air shipment."""
        return f"Tracking DHL Air shipment {self.tracking_number}"
    
    def get_estimated_delivery_time(self):
        """Get the estimated delivery time for the DHL air shipment."""
        return "1-2 business days" if self.express_air else "3-5 business days"
    
    def request_priority_handling(self):
        """Request priority handling for this shipment."""
        return True