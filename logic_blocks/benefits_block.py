"""
Benefits Logic Block
--------------------
Transforms product benefits into structured content.
"""

def generate_benefits(product: dict) -> list:
    return [
        f"{benefit} using {product['concentration']}"
        for benefit in product.get("benefits", [])
    ]
