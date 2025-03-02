#!/usr/bin/env python3
"""
Shipment System Demo
This script demonstrates the use of the Abstract Factory pattern
in a shipping system.
"""

from shipment_system.factories import DHLFactory, FedExFactory, UPSFactory
from shipment_system.products.dhl.dhl_air_shipment import DHLAirShipment
from shipment_system.products.fedex.fedex_ground_shipment import FedExGroundShipment
from shipment_system.products.ups.ups_water_shipment import UPSWaterShipment


def create_and_configure_shipment(factory_name, shipment_type, destination, weight, **kwargs):
    """Create and configure a shipment based on factory name and shipment type."""
    # Create the appropriate factory
    if factory_name.lower() == "dhl":
        factory = DHLFactory()
    elif factory_name.lower() == "fedex":
        factory = FedExFactory()
    elif factory_name.lower() == "ups":
        factory = UPSFactory()
    else:
        raise ValueError(f"Unknown factory: {factory_name}")
    
    # Create the appropriate shipment
    if shipment_type.lower() == "air":
        shipment = factory.create_air_shipment()
    elif shipment_type.lower() == "ground":
        shipment = factory.create_ground_shipment()
    elif shipment_type.lower() == "water":
        shipment = factory.create_water_shipment()
    else:
        raise ValueError(f"Unknown shipment type: {shipment_type}")
    
    # Configure the shipment
    shipment.set_destination(destination)
    shipment.set_weight(weight)
    
    # Handle special options based on shipment type
    # DHL options
    if isinstance(shipment, DHLAirShipment) and "express" in kwargs:
        shipment.set_express_air(kwargs["express"])
    
    # FedEx options
    if isinstance(shipment, FedExGroundShipment) and "local" in kwargs:
        shipment.set_local_delivery(kwargs["local"])
    
    # UPS options
    if isinstance(shipment, UPSWaterShipment) and "freight_forwarding" in kwargs:
        shipment.set_freight_forwarding(kwargs["freight_forwarding"])
    
    return shipment, factory


def print_shipment_info(shipment, factory):
    """Print information about a shipment and its factory."""
    print(f"\n{'-'*50}")
    print(f"Shipment Type: {shipment.__class__.__name__}")
    print(f"Tracking Number: {shipment.get_tracking_number()}")
    print(f"Destination: {shipment.get_destination()}")
    print(f"Weight: {shipment.get_weight()} kg")
    print(f"Cost: ${shipment.calculate_cost():.2f}")
    print(f"Tracking Status: {shipment.track_shipment()}")
    print(f"Estimated Delivery: {shipment.get_estimated_delivery_time()}")
    
    # Show factory-specific features
    if isinstance(factory, DHLFactory):
        print(f"Insurance Available: {factory.offer_insurance()}")
    elif isinstance(factory, FedExFactory):
        print(f"Priority Routing Available: {factory.priority_routing()}")
    elif isinstance(factory, UPSFactory):
        print(f"Saturday Delivery Available: {factory.saturday_delivery()}")


def main():
    """Main function to demonstrate the shipment system."""
    print("Shipment System Demo")
    print("===================")
    
    # Create some sample shipments
    shipments = [
        create_and_configure_shipment("DHL", "air", "Tokyo, Japan", 10.5, express=True),
        create_and_configure_shipment("FedEx", "ground", "Chicago, USA", 25.0, local=True),
        create_and_configure_shipment("UPS", "water", "Rotterdam, Netherlands", 1500.0, freight_forwarding=True)
    ]
    
    # Print information about each shipment
    for shipment, factory in shipments:
        print_shipment_info(shipment, factory)
    
    print("\nDemonstration of client code working with different factories:")
    print("-------------------------------------------------------------")
    
    # Example of client code that works with any factory
    for factory_class in [DHLFactory, FedExFactory, UPSFactory]:
        factory = factory_class()
        
        # Create an air shipment regardless of the factory type
        air_shipment = factory.create_air_shipment()
        air_shipment.set_destination("Paris, France")
        air_shipment.set_weight(5.0)
        
        print(f"\n{factory_class.__name__} created:")
        print(f"Tracking: {air_shipment.get_tracking_number()}")
        print(f"Cost: ${air_shipment.calculate_cost():.2f}")
        print(f"Delivery Time: {air_shipment.get_estimated_delivery_time()}")


if __name__ == "__main__":
    main()