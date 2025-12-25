"""
Usage Logic Block
-----------------
Generates usage instructions.
"""

def generate_usage(product: dict) -> str:
    return product.get("usage", "")
