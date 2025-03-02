from shipment_system.abstract.shipment_factory import ShipmentFactory
from shipment_system.products.dhl.dhl_air_shipment import DHLAirShipment
from shipment_system.products.dhl.dhl_ground_shipment import DHLGroundShipment
from shipment_system.products.dhl.dhl_water_shipment import DHLWaterShipment

class DHLFactory(ShipmentFactory):
    """DHL concrete factory implementation."""
    
    def create_air_shipment(self):
        """Create a DHL air shipment."""
        return DHLAirShipment()
    
    def create_ground_shipment(self):
        """Create a DHL ground shipment."""
        return DHLGroundShipment()
    
    def create_water_shipment(self):
        """Create a DHL water shipment."""
        return DHLWaterShipment()
    
    def offer_insurance(self):
        """DHL-specific method to offer insurance."""
        return True