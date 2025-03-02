from shipment_system.abstract.shipment import Shipment

class UPSWaterShipment(Shipment):
    """UPS Water Shipment implementation."""
    
    def __init__(self):
        super().__init__()
        self.freight_forwarding = False
    
    def set_freight_forwarding(self, freight_forwarding):
        """Set whether this shipment uses freight forwarding."""
        self.freight_forwarding = freight_forwarding
    
    def calculate_cost(self):
        """Calculate the cost of the UPS water shipment."""
        base_cost = 190.0 + (self.weight * 0.85)
        return base_cost * 1.25 if self.freight_forwarding else base_cost
    
    def track_shipment(self):
        """Track the UPS water shipment."""
        return f"Tracking UPS Water shipment {self.tracking_number}"
    
    def get_estimated_delivery_time(self):
        """Get the estimated delivery time for the UPS water shipment."""
        return "18-28 business days"
    
    def request_port_to_port_service(self):
        """Request port-to-port service for this shipment."""
        return True