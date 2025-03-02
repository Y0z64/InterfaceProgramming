from shipment_system.abstract.shipment_factory import ShipmentFactory
from shipment_system.products.fedex.fedex_air_shipment import FedExAirShipment
from shipment_system.products.fedex.fedex_ground_shipment import FedExGroundShipment
from shipment_system.products.fedex.fedex_water_shipment import FedExWaterShipment

class FedExFactory(ShipmentFactory):
    """FedEx concrete factory implementation."""
    
    def create_air_shipment(self):
        """Create a FedEx air shipment."""
        return FedExAirShipment()
    
    def create_ground_shipment(self):
        """Create a FedEx ground shipment."""
        return FedExGroundShipment()
    
    def create_water_shipment(self):
        """Create a FedEx water shipment."""
        return FedExWaterShipment()
    
    def priority_routing(self):
        """FedEx-specific method to offer priority routing."""
        return True