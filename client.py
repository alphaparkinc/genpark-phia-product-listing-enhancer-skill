"""
genpark-phia-product-listing-enhancer-skill: Client SDK
Extracts structured values from messy specs.
"""
from __future__ import annotations
from typing import Optional


class PhiaProductListingEnhancerClient:
    """
    SDK for phia-like product parsing.
    """

    def enrich_listing(
        self,
        unstructured_specs: str,
        product_name: str,
    ) -> dict:
        text = unstructured_specs.lower()
        
        # Simple rule-based extraction
        weight = 1.0
        if "lbs" in text:
            try:
                parts = text.split("lbs")
                weight = float(parts[0].split()[-1])
            except Exception:
                pass

        packaging = "Standard Box"
        if "eco" in text or "biodegradable" in text:
            packaging = "Eco Friendly Box"

        return {
            "enriched_product_details": {
                "product_name": product_name,
                "weight_lbs": weight,
                "packaging": packaging,
                "extraction_confidence": 0.95
            }
        }
