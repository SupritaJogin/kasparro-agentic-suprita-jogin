from agents.base_agent import BaseAgent

class ContentGenerationAgent(BaseAgent):
    """
    Agent responsible for generating content from parsed product data.
    """

    def handle(self, task: dict):
        if task.get("type") != "PARSED_PRODUCT":
            return None

        product = task.get("payload")

        content = {
            "title": product["name"],
            "description": f"The {product['name']} is a premium product in the {product['category']} category.",
            "price": product["price"]
        }

        return {
            "type": "GENERATED_CONTENT",
            "payload": content
        }
