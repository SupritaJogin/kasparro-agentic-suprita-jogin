"""
ProductParserAgent
------------------
Responsibility:
- Accept raw product data
- Validate required fields
- Normalize structure for downstream agents
"""

class ProductParserAgent:
    REQUIRED_FIELDS = [
        "name",
        "concentration",
        "skin_type",
        "key_ingredients",
        "benefits",
        "how_to_use",
        "side_effects",
        "price"
    ]

    def parse(self, product_data: dict) -> dict:
        """
        Parses and validates raw product data.
        Returns a clean internal representation.
        """
        self._validate(product_data)

        parsed_data = {
            "name": product_data["name"],
            "concentration": product_data["concentration"],
            "skin_type": product_data["skin_type"],
            "ingredients": product_data["key_ingredients"],
            "benefits": product_data["benefits"],
            "usage": product_data["how_to_use"],
            "side_effects": product_data["side_effects"],
            "price": product_data["price"]
        }

        return parsed_data

    def _validate(self, product_data: dict):
        missing = [
            field for field in self.REQUIRED_FIELDS
            if field not in product_data
        ]
        if missing:
            raise ValueError(f"Missing required fields: {missing}")

