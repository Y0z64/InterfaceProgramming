from shipment_system.abstract.shipment import Shipment

class DHLGroundShipment(Shipment):
    """DHL Ground Shipment implementation."""
    
    def __init__(self):
        super().__init__()
        self.route_optimization = False
    
    def set_route_optimization(self, route_optimization):
        """Set whether route optimization is enabled."""
        self.route_optimization = route_optimization
    
    def calculate_cost(self):
        """Calculate the cost of the DHL ground shipment."""
        base_cost = 50.0 + (self.weight * 1.2)
        return base_cost * 1.1 if self.route_optimization else base_cost
    
    def track_shipment(self):
        """Track the DHL ground shipment."""
        return f"Tracking DHL Ground shipment {self.tracking_number}"
    
    def get_estimated_delivery_time(self):
        """Get the estimated delivery time for the DHL ground shipment."""
        return "2-3 business days" if self.route_optimization else "4-7 business days"
    
    def request_signature_on_delivery(self):
        """Request signature on delivery for this shipment."""
        return True