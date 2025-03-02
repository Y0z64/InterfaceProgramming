from shipment_system.abstract.shipment import Shipment

class FedExWaterShipment(Shipment):
    """FedEx Water Shipment implementation."""
    
    def __init__(self):
        super().__init__()
        self.international_shipping = False
    
    def set_international_shipping(self, international_shipping):
        """Set whether this is an international shipping."""
        self.international_shipping = international_shipping
    
    def calculate_cost(self):
        """Calculate the cost of the FedEx water shipment."""
        base_cost = 180.0 + (self.weight * 0.9)
        return base_cost * 1.4 if self.international_shipping else base_cost
    
    def track_shipment(self):
        """Track the FedEx water shipment."""
        return f"Tracking FedEx Water shipment {self.tracking_number}"
    
    def get_estimated_delivery_time(self):
        """Get the estimated delivery time for the FedEx water shipment."""
        return "20-35 business days" if self.international_shipping else "15-25 business days"
    
    def request_large_item_handling(self):
        """Request large item handling for this shipment."""
        return True