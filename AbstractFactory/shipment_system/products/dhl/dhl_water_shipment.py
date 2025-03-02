from shipment_system.abstract.shipment import Shipment

class DHLWaterShipment(Shipment):
    """DHL Water Shipment implementation."""
    
    def __init__(self):
        super().__init__()
        self.container_type = "Standard"
    
    def set_container_type(self, container_type):
        """Set the container type for this shipment."""
        self.container_type = container_type
    
    def calculate_cost(self):
        """Calculate the cost of the DHL water shipment."""
        base_cost = 200.0 + (self.weight * 0.8)
        return base_cost * 1.3 if self.container_type == "Premium" else base_cost
    
    def track_shipment(self):
        """Track the DHL water shipment."""
        return f"Tracking DHL Water shipment {self.tracking_number}"
    
    def get_estimated_delivery_time(self):
        """Get the estimated delivery time for the DHL water shipment."""
        return "15-30 business days"
    
    def request_customs_clearance(self):
        """Request customs clearance for this shipment."""
        return True