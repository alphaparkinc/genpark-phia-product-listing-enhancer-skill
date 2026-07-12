"""
example_usage.py -- Demonstrates PhiaProductListingEnhancerClient
"""
from client import PhiaProductListingEnhancerClient

def main():
    client = PhiaProductListingEnhancerClient()
    result = client.enrich_listing(
        unstructured_specs="The item weighs 4.5lbs. Made of recyclable materials, shipped in eco friendly box.",
        product_name="Glow Kit"
    )
    print("[Phia Listing Enhancer Result]")
    print(result['enriched_product_details'])

if __name__ == "__main__":
    main()
