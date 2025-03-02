from shipment_system.abstract.shipment import Shipment

class UPSAirShipment(Shipment):
    """UPS Air Shipment implementation."""
    
    def __init__(self):
        super().__init__()
        self.next_day_air = False
    
    def set_next_day_air(self, next_day_air):
        """Set whether this is a next-day air shipment."""
        self.next_day_air = next_day_air
    
    def calculate_cost(self):
        """Calculate the cost of the UPS air shipment."""
        base_cost = 110.0 + (self.weight * 2.6)
        return base_cost * 1.8 if self.next_day_air else base_cost
    
    def track_shipment(self):
        """Track the UPS air shipment."""
        return f"Tracking UPS Air shipment {self.tracking_number}"
    
    def get_estimated_delivery_time(self):
        """Get the estimated delivery time for the UPS air shipment."""
        return "Next business day" if self.next_day_air else "2-4 business days"
    
    def request_carbon_neutral_shipping(self):
        """Request carbon-neutral shipping for this shipment."""
        return True