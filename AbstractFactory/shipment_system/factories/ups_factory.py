from shipment_system.abstract.shipment_factory import ShipmentFactory
from shipment_system.products.ups.ups_air_shipment import UPSAirShipment
from shipment_system.products.ups.ups_ground_shipment import UPSGroundShipment
from shipment_system.products.ups.ups_water_shipment import UPSWaterShipment

class UPSFactory(ShipmentFactory):
    """UPS concrete factory implementation."""
    
    def create_air_shipment(self):
        """Create a UPS air shipment."""
        return UPSAirShipment()
    
    def create_ground_shipment(self):
        """Create a UPS ground shipment."""
        return UPSGroundShipment()
    
    def create_water_shipment(self):
        """Create a UPS water shipment."""
        return UPSWaterShipment()
    
    def saturday_delivery(self):
        """UPS-specific method to offer Saturday delivery."""
        return True