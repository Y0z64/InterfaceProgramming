from shipment_system.abstract.shipment import Shipment

class UPSGroundShipment(Shipment):
    """UPS Ground Shipment implementation."""
    
    def __init__(self):
        super().__init__()
        self.ground_saver = False
    
    def set_ground_saver(self, ground_saver):
        """Set whether this is a ground saver shipment."""
        self.ground_saver = ground_saver
    
    def calculate_cost(self):
        """Calculate the cost of the UPS ground shipment."""
        base_cost = 55.0 + (self.weight * 1.3)
        return base_cost * 0.85 if self.ground_saver else base_cost
    
    def track_shipment(self):
        """Track the UPS ground shipment."""
        return f"Tracking UPS Ground shipment {self.tracking_number}"
    
    def get_estimated_delivery_time(self):
        """Get the estimated delivery time for the UPS ground shipment."""
        return "4-6 business days" if self.ground_saver else "2-5 business days"
    
    def request_address_correction(self):
        """Request address correction for this shipment."""
        return True