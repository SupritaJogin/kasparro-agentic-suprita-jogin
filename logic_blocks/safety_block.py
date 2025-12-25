"""
Safety Logic Block
------------------
Generates safety-related information.
"""

def generate_safety(product: dict) -> dict:
    return {
        "side_effects": product.get("side_effects", ""),
        "recommended_for_sensitive_skin": "Yes" if "Mild" in product.get("side_effects", "") else "No"
    }
