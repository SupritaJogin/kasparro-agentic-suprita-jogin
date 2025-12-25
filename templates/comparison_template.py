"""
Comparison Template
-------------------
Builds comparison page JSON.
"""

def build_comparison_page(product_a: dict, product_b: dict) -> dict:
    return {
        "page_type": "Comparison",
        "product_a": {
            "name": product_a["name"],
            "price": product_a["price"],
            "benefits": product_a["benefits"]
        },
        "product_b": {
            "name": product_b["name"],
            "price": product_b["price"],
            "benefits": product_b["benefits"]
        },
        "comparison_summary": "Product A focuses on brightening while Product B targets hydration."
    }
