from agents.base_agent import BaseAgent

class ProductParserAgent(BaseAgent):
    """
    Agent responsible for validating and normalizing raw product data.
    """

    def handle(self, task: dict):
        # This agent only handles product parsing tasks
        if task.get("type") != "PARSE_PRODUCT":
            return None

        product = task.get("payload", {})

        # Basic validation
        required_fields = ["name", "price", "category"]
        for field in required_fields:
            if field not in product:
                raise ValueError(f"Missing required field: {field}")

        # Normalization step (example)
        normalized_product = {
            "name": product["name"].strip(),
            "price": float(product["price"]),
            "category": product["category"].lower()
        }

        # Return a NEW message (agent autonomy)
        return {
            "type": "PARSED_PRODUCT",
            "payload": normalized_product
        }
