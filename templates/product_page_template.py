"""
Product Page Template
---------------------
Builds product page JSON using logic blocks.
"""

from logic_blocks.benefits_block import generate_benefits
from logic_blocks.usage_block import generate_usage
from logic_blocks.safety_block import generate_safety

def build_product_page(product: dict) -> dict:
    return {
        "page_type": "Product",
        "name": product["name"],
        "concentration": product["concentration"],
        "ingredients": product["ingredients"],
        "benefits": generate_benefits(product),
        "usage": generate_usage(product),
        "safety": generate_safety(product),
        "price": product["price"]
    }
